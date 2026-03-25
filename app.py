import os
import io
import csv
import json
from functools import wraps
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import db, User, Submission
from problems import PROBLEMS
from judge import judge_submission

app = Flask(__name__)
app.config['SECRET_KEY'] = 'python-judge-secret-key-2024'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///judge.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Vui lòng đăng nhập để tiếp tục.'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('problem_list'))
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        if current_user.is_admin:
            return redirect(url_for('admin_dashboard'))
        return redirect(url_for('problem_list'))
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            flash('Đăng nhập thành công!', 'success')
            if user.is_admin:
                return redirect(url_for('admin_dashboard'))
            return redirect(url_for('problem_list'))
        else:
            flash('Tên đăng nhập hoặc mật khẩu không đúng.', 'error')
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('problem_list'))
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        fullname = request.form.get('fullname', '').strip()
        password = request.form.get('password', '')
        confirm = request.form.get('confirm', '')

        if not username or not fullname or not password:
            flash('Vui lòng điền đầy đủ thông tin.', 'error')
        elif len(username) < 3:
            flash('Tên đăng nhập phải có ít nhất 3 ký tự.', 'error')
        elif len(password) < 4:
            flash('Mật khẩu phải có ít nhất 4 ký tự.', 'error')
        elif password != confirm:
            flash('Mật khẩu xác nhận không khớp.', 'error')
        elif User.query.filter_by(username=username).first():
            flash('Tên đăng nhập đã tồn tại.', 'error')
        else:
            user = User(username=username, fullname=fullname)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            flash('Đăng ký thành công! Vui lòng đăng nhập.', 'success')
            return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Đã đăng xuất.', 'success')
    return redirect(url_for('login'))


@app.route('/problems')
@login_required
def problem_list():
    # Get best scores per problem for current user
    best_scores = {}
    for pid in PROBLEMS:
        best = Submission.query.filter_by(
            user_id=current_user.id, problem_id=pid
        ).order_by(Submission.score.desc()).first()
        best_scores[pid] = best.score if best else None
    return render_template('problems.html', problems=PROBLEMS, best_scores=best_scores)


@app.route('/problem/<int:pid>')
@login_required
def problem_detail(pid):
    if pid not in PROBLEMS:
        flash('Bài tập không tồn tại.', 'error')
        return redirect(url_for('problem_list'))
    problem = PROBLEMS[pid]
    # Get recent submissions
    submissions = Submission.query.filter_by(
        user_id=current_user.id, problem_id=pid
    ).order_by(Submission.submitted_at.desc()).limit(10).all()
    return render_template('problem_detail.html', problem=problem, submissions=submissions)


@app.route('/submit/<int:pid>', methods=['POST'])
@login_required
def submit(pid):
    if pid not in PROBLEMS:
        flash('Bài tập không tồn tại.', 'error')
        return redirect(url_for('problem_list'))

    code = request.form.get('code', '')
    if not code.strip():
        flash('Vui lòng nhập code trước khi nộp.', 'error')
        return redirect(url_for('problem_detail', pid=pid))

    # Judge the submission
    result = judge_submission(pid, code)

    # Save to database
    sub = Submission(
        user_id=current_user.id,
        problem_id=pid,
        code=code,
        score=result['score'],
        total=result['total'],
        details=json.dumps(result['details'], ensure_ascii=False),
    )
    db.session.add(sub)
    db.session.commit()

    return redirect(url_for('submission_result', sid=sub.id))


@app.route('/result/<int:sid>')
@login_required
def submission_result(sid):
    sub = Submission.query.get_or_404(sid)
    if sub.user_id != current_user.id:
        flash('Bạn không có quyền xem kết quả này.', 'error')
        return redirect(url_for('problem_list'))
    problem = PROBLEMS.get(sub.problem_id, {})
    details = json.loads(sub.details) if sub.details else []
    return render_template('results.html', submission=sub, problem=problem, details=details)


@app.route('/scoreboard')
@login_required
def scoreboard():
    users = User.query.filter_by(is_admin=False).all()
    board = []
    for u in users:
        total = 0
        solved = 0
        for pid in PROBLEMS:
            best = Submission.query.filter_by(
                user_id=u.id, problem_id=pid
            ).order_by(Submission.score.desc()).first()
            if best:
                total += best.score
                if best.score == 100:
                    solved += 1
        board.append({
            'username': u.username,
            'fullname': u.fullname,
            'total_score': total,
            'solved': solved,
        })
    board.sort(key=lambda x: (-x['total_score'], -x['solved'], x['fullname']))
    return render_template('scoreboard.html', board=board, total_problems=len(PROBLEMS))


# ============ ADMIN ROUTES ============

def admin_required(f):
    @wraps(f)
    @login_required
    def decorated(*args, **kwargs):
        if not current_user.is_admin:
            flash('Bạn không có quyền truy cập trang này.', 'error')
            return redirect(url_for('problem_list'))
        return f(*args, **kwargs)
    return decorated


@app.route('/admin')
@admin_required
def admin_dashboard():
    students = User.query.filter_by(is_admin=False).order_by(User.fullname).all()
    # Build score matrix
    student_data = []
    for s in students:
        scores = {}
        total = 0
        for pid in PROBLEMS:
            best = Submission.query.filter_by(
                user_id=s.id, problem_id=pid
            ).order_by(Submission.score.desc()).first()
            sc = best.score if best else None
            scores[pid] = sc
            if sc:
                total += sc
        student_data.append({
            'user': s,
            'scores': scores,
            'total': total,
        })
    student_data.sort(key=lambda x: -x['total'])
    return render_template('admin_dashboard.html', student_data=student_data, problems=PROBLEMS)


@app.route('/admin/create-account', methods=['GET', 'POST'])
@admin_required
def admin_create_account():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        fullname = request.form.get('fullname', '').strip()
        password = request.form.get('password', '').strip()

        if not username or not fullname or not password:
            flash('Vui lòng điền đầy đủ thông tin.', 'error')
        elif User.query.filter_by(username=username).first():
            flash(f'Tên đăng nhập "{username}" đã tồn tại.', 'error')
        else:
            user = User(username=username, fullname=fullname)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            flash(f'Tạo tài khoản "{username}" thành công!', 'success')
            return redirect(url_for('admin_dashboard'))
    return render_template('admin_create_account.html')


@app.route('/admin/bulk-upload', methods=['GET', 'POST'])
@admin_required
def admin_bulk_upload():
    if request.method == 'POST':
        file = request.files.get('csv_file')
        if not file or not file.filename:
            flash('Vui lòng chọn file CSV.', 'error')
            return render_template('admin_bulk_upload.html')

        try:
            stream = io.StringIO(file.stream.read().decode('utf-8-sig'))
            reader = csv.reader(stream)
            created = 0
            skipped = 0
            errors = []
            for row_num, row in enumerate(reader, 1):
                if not row or len(row) < 3:
                    errors.append(f'Dòng {row_num}: thiếu dữ liệu')
                    continue
                username = row[0].strip()
                fullname = row[1].strip()
                password = row[2].strip()
                if not username or not fullname or not password:
                    errors.append(f'Dòng {row_num}: dữ liệu trống')
                    continue
                if User.query.filter_by(username=username).first():
                    skipped += 1
                    errors.append(f'Dòng {row_num}: "{username}" đã tồn tại → bỏ qua')
                    continue
                user = User(username=username, fullname=fullname)
                user.set_password(password)
                db.session.add(user)
                created += 1
            db.session.commit()
            flash(f'Đã tạo {created} tài khoản. Bỏ qua {skipped} (đã tồn tại).', 'success')
            if errors:
                flash('Chi tiết: ' + '; '.join(errors[:10]), 'error')
            return redirect(url_for('admin_dashboard'))
        except Exception as e:
            flash(f'Lỗi đọc file: {str(e)}', 'error')
    return render_template('admin_bulk_upload.html')


with app.app_context():
    db.create_all()
    # Create default admin if not exists
    if not User.query.filter_by(username='admin').first():
        admin = User(username='admin', fullname='Quản trị viên', is_admin=True)
        admin.set_password('admin123')
        db.session.add(admin)
        db.session.commit()


if __name__ == '__main__':
    app.run(debug=True, port=5000)
