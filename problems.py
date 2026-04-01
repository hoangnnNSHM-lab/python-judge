"""Problem definitions for the Python Lambda Judge."""

MODULES = {
    'lambda': {
        'id': 'lambda',
        'title': 'Hàm nâng cao (Lambda)',
        'description': 'Các bài tập sử dụng lambda, map, filter và các hàm bậc cao trong Python.',
        'icon': 'λ'
    },
    'basics': {
        'id': 'basics',
        'title': 'Python Cơ bản',
        'description': 'Các bài tập nhập môn, biến, kiểu dữ liệu, vòng lặp và câu lệnh điều kiện.',
        'icon': '🐍'
    },
    'review_apr': {
        'id': 'review_apr',
        'title': 'Ôn tập tháng 4',
        'description': 'Đề kiểm tra thực hành lập trình Python: Xử lý Chuỗi (String), Danh sách (List) và Hàm ẩn danh (Lambda). Thời gian: 90 phút.',
        'icon': '📝'
    }
}

PROBLEMS = {
    1: {
        'id': 1,
        'module_id': 'lambda',
        'title': 'Tính biểu thức tuyến tính',
        'difficulty': 'Cơ bản',
        'difficulty_color': '#4ade80',
        'category': 'Toán học',
        'description': '''Viết một chương trình sử dụng hàm <code>lambda</code> để tính nhanh giá trị của hàm số bậc nhất <strong>f(x) = ax + b</strong>.''',
        'input_desc': 'Một dòng duy nhất chứa 3 số nguyên a, x, b cách nhau bởi một khoảng trắng (-10⁴ ≤ a, x, b ≤ 10⁴).',
        'output_desc': 'In ra một số nguyên duy nhất là kết quả của biểu thức ax + b.',
        'example_input': '5 2 10',
        'example_output': '20',
        'explanation': 'f(2) = 5×2 + 10 = 20',
    },
    2: {
        'id': 2,
        'module_id': 'lambda',
        'title': 'Tính tổng bình phương số chẵn',
        'difficulty': 'Trung bình',
        'difficulty_color': '#facc15',
        'category': 'Toán học',
        'description': '''Cho một dãy số nguyên. Yêu cầu kết hợp hàm <code>filter()</code>, <code>map()</code> và <code>lambda</code> để lọc ra các số chẵn, sau đó tính bình phương của chúng và in ra tổng cuối cùng.''',
        'input_desc': 'Một dòng chứa N số nguyên, các số cách nhau bởi một khoảng trắng (1 ≤ N ≤ 10⁵).',
        'output_desc': 'Một số nguyên dương duy nhất là tổng bình phương của các số chẵn có trong mảng. Nếu không có số chẵn nào, in ra 0.',
        'example_input': '1 2 3 4 5',
        'example_output': '20',
        'explanation': 'Các số chẵn là 2 và 4. Tổng bình phương: 2² + 4² = 4 + 16 = 20.',
    },
    3: {
        'id': 3,
        'module_id': 'lambda',
        'title': 'Tìm số có tổng chữ số lớn nhất',
        'difficulty': 'Trung bình',
        'difficulty_color': '#facc15',
        'category': 'Toán học',
        'description': '''Cho danh sách các số nguyên dương. Hãy tìm số có tổng các chữ số cấu thành lên nó là lớn nhất. Sử dụng hàm <code>max()</code> kết hợp với thuộc tính <code>key=lambda</code>. Nếu có nhiều số cùng tổng lớn nhất, lấy số xuất hiện đầu tiên trong danh sách.''',
        'input_desc': 'Một dòng chứa N số nguyên dương cách nhau bởi khoảng trắng.',
        'output_desc': 'In ra số nguyên thỏa mãn điều kiện bài toán.',
        'example_input': '15 8 29 111',
        'example_output': '29',
        'explanation': 'Tổng chữ số: 15→6, 8→8, 29→11, 111→3. Số 29 có tổng chữ số lớn nhất (11).',
    },
    4: {
        'id': 4,
        'module_id': 'lambda',
        'title': 'Sắp xếp theo giá trị tuyệt đối',
        'difficulty': 'Khá',
        'difficulty_color': '#fb923c',
        'category': 'Toán học',
        'description': '''Cho một mảng số nguyên. Hãy sắp xếp mảng theo giá trị tuyệt đối tăng dần. Trong trường hợp hai số có cùng giá trị tuyệt đối (ví dụ -5 và 5), số âm phải được ưu tiên xếp trước số dương. Sử dụng <code>sort()</code> hoặc <code>sorted()</code> với <code>key=lambda</code>.''',
        'input_desc': 'Một dòng chứa các số nguyên cách nhau bởi khoảng trắng.',
        'output_desc': 'Mảng sau khi đã được sắp xếp, các phần tử cách nhau bởi một khoảng trắng.',
        'example_input': '4 -1 3 -4 2 -3',
        'example_output': '-1 2 -3 3 -4 4',
        'explanation': 'Sắp xếp theo |x| tăng dần, nếu bằng nhau thì số âm đứng trước.',
    },
    5: {
        'id': 5,
        'module_id': 'lambda',
        'title': 'Không gian Oxy và Khoảng cách',
        'difficulty': 'Nâng cao',
        'difficulty_color': '#f87171',
        'category': 'Toán học',
        'description': '''Cho danh sách tọa độ của N điểm trên mặt phẳng Descartes. Hãy sắp xếp các điểm này theo khoảng cách từ điểm đó tới gốc tọa độ (0,0) tăng dần. Nếu 2 điểm có cùng khoảng cách tới gốc, điểm nào có hoành độ (x) nhỏ hơn sẽ đứng trước.<br><em>Khoảng cách từ (x,y) đến (0,0) được tính bằng x² + y² (không cần khai căn).</em>''',
        'input_desc': 'Dòng đầu chứa số nguyên N (1 ≤ N ≤ 10⁴). N dòng tiếp theo, mỗi dòng chứa 2 số nguyên x, y là tọa độ của một điểm.',
        'output_desc': 'N dòng, mỗi dòng in ra tọa độ x, y sau khi đã sắp xếp.',
        'example_input': '3\n1 3\n-2 2\n3 1',
        'example_output': '-2 2\n1 3\n3 1',
        'explanation': 'Khoảng cách: (-2,2)→8, (1,3)→10, (3,1)→10. Vì (1,3) và (3,1) cùng khoảng cách, x=1 < x=3 nên (1,3) đứng trước.',
    },
    6: {
        'id': 6,
        'module_id': 'lambda',
        'title': 'Quy đổi nhiệt độ IoT',
        'difficulty': 'Cơ bản',
        'difficulty_color': '#4ade80',
        'category': 'Thực tế',
        'description': '''Một hệ thống cảm biến trả về danh sách nhiệt độ đo bằng độ Celsius (C). Bạn cần dùng <code>map()</code> và <code>lambda</code> để chuyển đổi toàn bộ danh sách này sang độ Fahrenheit (F) theo công thức <strong>F = C × 1.8 + 32</strong>.''',
        'input_desc': 'Một dòng chứa các số thực (độ C) cách nhau bởi khoảng trắng.',
        'output_desc': 'Các số thực (độ F) cách nhau bởi khoảng trắng, làm tròn chính xác 1 chữ số thập phân.',
        'example_input': '25 30 0 -10.5',
        'example_output': '77.0 86.0 32.0 13.1',
        'explanation': '25°C = 25×1.8+32 = 77.0°F, 30°C = 86.0°F, 0°C = 32.0°F, -10.5°C = 13.1°F',
    },
    7: {
        'id': 7,
        'module_id': 'lambda',
        'title': 'Rút trích Tên miền Email',
        'difficulty': 'Trung bình',
        'difficulty_color': '#facc15',
        'category': 'Thực tế',
        'description': '''Hệ thống Marketing thu thập được một danh sách các địa chỉ email của khách hàng. Bạn cần viết một biểu thức để lấy ra các <strong>tên miền (domain)</strong> (phần nằm ngay sau ký tự <code>@</code>). Sau đó lọc bỏ các tên miền trùng lặp và in ra kết quả theo thứ tự từ điển (A-Z).''',
        'input_desc': 'Một chuỗi duy nhất chứa các địa chỉ email, cách nhau bởi dấu phẩy ",".',
        'output_desc': 'Tên miền duy nhất, cách nhau bởi khoảng trắng và đã sắp xếp alphabet.',
        'example_input': 'an@gmail.com,binh@yahoo.com,chau@gmail.com,duy@edu.vn',
        'example_output': 'edu.vn gmail.com yahoo.com',
        'explanation': 'Trích domain: gmail.com, yahoo.com, gmail.com, edu.vn → Unique + Sort: edu.vn gmail.com yahoo.com',
    },
    8: {
        'id': 8,
        'module_id': 'lambda',
        'title': 'Trích xuất Log Lỗi Máy chủ',
        'difficulty': 'Trung bình',
        'difficulty_color': '#facc15',
        'category': 'Thực tế',
        'description': '''Trong file nhật ký (Log) của Server, mỗi dòng có cấu trúc: <code>[Mức_độ] Nội_dung_thông_báo</code>. Bạn hãy kết hợp <code>filter()</code> và <code>lambda</code> để chỉ trích xuất những dòng log có mức độ là <code>[ERROR]</code> để đội kỹ thuật xử lý.''',
        'input_desc': 'Dòng đầu là số lượng log N. N dòng tiếp theo là các chuỗi log tương ứng.',
        'output_desc': 'In ra đúng các dòng chứa từ khóa [ERROR] ở đầu, giữ nguyên thứ tự ban đầu.',
        'example_input': '3\n[INFO] User logged in\n[ERROR] Database timeout\n[WARN] High memory',
        'example_output': '[ERROR] Database timeout',
        'explanation': 'Chỉ dòng "[ERROR] Database timeout" bắt đầu bằng [ERROR].',
    },
    9: {
        'id': 9,
        'module_id': 'lambda',
        'title': 'Xếp hạng Xét tuyển Đại học',
        'difficulty': 'Khá',
        'difficulty_color': '#fb923c',
        'category': 'Thực tế',
        'description': '''Xét tuyển đại học cho sinh viên theo tổ hợp điểm (Toán, Văn). Bạn cần sắp xếp danh sách học sinh theo cơ chế ưu tiên:<br>
        <strong>1.</strong> Tổng điểm Toán + Văn giảm dần;<br>
        <strong>2.</strong> Nếu tổng điểm bằng nhau, ưu tiên điểm Toán cao hơn;<br>
        <strong>3.</strong> Nếu vẫn bằng nhau, xếp tên theo bảng chữ cái A-Z.''',
        'input_desc': 'Dòng đầu là số lượng thí sinh N. N dòng sau, mỗi dòng gồm: Tên Điểm_Toán Điểm_Văn (Tên viết liền không dấu cách).',
        'output_desc': 'Tên của các học sinh sau khi đã sắp xếp thứ hạng, mỗi tên trên một dòng.',
        'example_input': '4\nAn 8 7\nBao 7 8\nCuong 9 8\nDung 8 7',
        'example_output': 'Cuong\nAn\nDung\nBao',
        'explanation': 'Cuong tổng 17 lớn nhất. An & Bao cùng tổng 15, An có Toán cao hơn. An & Dung bằng cả tổng lẫn Toán → xếp tên A-Z.',
    },
    10: {
        'id': 10,
        'module_id': 'lambda',
        'title': 'Xử lý giỏ hàng Thương mại điện tử',
        'difficulty': 'Nâng cao',
        'difficulty_color': '#f87171',
        'category': 'Thực tế',
        'description': '''Một App mua sắm gửi giỏ hàng về Backend dưới dạng chuỗi đóng gói. Bạn cần loại bỏ các mặt hàng có <strong>Số lượng = 0</strong>. Sau đó tính Tổng số tiền của các mặt hàng còn lại. Áp dụng quy tắc: Nếu tổng số tiền mua sắm <strong>≥ 1000$</strong>, giảm giá 10% trên tổng hóa đơn.<br><em>Thách thức: Giải quyết bằng lambda kết hợp map/filter/sum.</em>''',
        'input_desc': 'Chuỗi các sản phẩm phân tách bởi dấu phẩy. Cấu trúc mỗi sản phẩm là MãSP:ĐơnGiá:SốLượng (ĐơnGiá và SốLượng là số nguyên).',
        'output_desc': 'Tổng số tiền phải thanh toán (Số nguyên, nếu có phần thập phân thì làm tròn xuống thành số nguyên).',
        'example_input': 'SP1:200:2,SP2:100:0,SP3:250:3',
        'example_output': '1035',
        'explanation': 'SP2 bị loại (SL=0). Tổng: (200×2)+(250×3)=1150. Vì 1150 ≥ 1000, giảm 10% → 1150×0.9 = 1035.',
    },

    11: {
        'id': 11,
        'module_id': 'basics',
        'title': 'Tính tổng hai số',
        'difficulty': 'Cơ bản',
        'difficulty_color': '#4ade80',
        'category': 'Cơ bản',
        'description': 'Viết chương trình nhập vào hai số nguyên A và B, in ra tổng của chúng.',
        'input_desc': 'Một dòng chứa 2 số nguyên cách nhau một khoảng trắng.',
        'output_desc': 'In ra tổng của hai số đó.',
        'example_input': '3 5',
        'example_output': '8',
        'explanation': '3 + 5 = 8'
    },
    12: {
        'id': 12,
        'module_id': 'basics',
        'title': 'Kiểm tra chẵn lẻ',
        'difficulty': 'Cơ bản',
        'difficulty_color': '#4ade80',
        'category': 'Cơ bản',
        'description': 'Cho một số nguyên n. In ra "YES" nếu n là số chẵn, ngược lại in ra "NO".',
        'input_desc': 'Một số nguyên n duy nhất.',
        'output_desc': '"YES" hoặc "NO"',
        'example_input': '4',
        'example_output': 'YES',
        'explanation': '4 là số chẵn nên in YES.'
    },

    # === ÔN TẬP THÁNG 4 ===
    13: {
        'id': 13,
        'module_id': 'review_apr',
        'title': 'Chuẩn hóa chuỗi',
        'difficulty': 'Cơ bản',
        'difficulty_color': '#4ade80',
        'category': 'Chuỗi',
        'description': '''Viết chương trình nhập vào một xâu ký tự họ và tên. Hãy chuẩn hóa xâu ký tự đó theo quy tắc:
<ul>
<li>Loại bỏ các khoảng trắng thừa ở đầu, cuối xâu.</li>
<li>Giữa các từ chỉ giữ lại đúng một khoảng trắng.</li>
<li>Chữ cái đầu tiên của mỗi từ phải được viết hoa, các chữ cái còn lại viết thường.</li>
</ul>''',
        'input_desc': 'Một dòng duy nhất chứa xâu ký tự S (độ dài không quá 1000 ký tự).',
        'output_desc': 'Xâu S sau khi đã được chuẩn hóa.',
        'example_input': '  nguYen   vAn    a ',
        'example_output': 'Nguyen Van A',
        'explanation': 'Loại bỏ khoảng trắng thừa, viết hoa chữ cái đầu mỗi từ.',
    },
    14: {
        'id': 14,
        'module_id': 'review_apr',
        'title': 'Lọc dữ liệu',
        'difficulty': 'Trung bình',
        'difficulty_color': '#facc15',
        'category': 'Danh sách',
        'description': '''Cho một danh sách gồm N số nguyên. Sử dụng tính năng List Comprehension hoặc các hàm <code>filter()</code>, <code>map()</code> kết hợp với biểu thức <code>lambda</code> để tạo và in ra một danh sách mới. Danh sách mới này chỉ chứa <strong>bình phương của các số lẻ</strong> có trong danh sách ban đầu.''',
        'input_desc': 'Dòng đầu tiên chứa số nguyên dương N (1 ≤ N ≤ 10⁵). Dòng thứ hai chứa N số nguyên, các số cách nhau bởi một khoảng trắng.',
        'output_desc': 'Các phần tử của danh sách mới, cách nhau bởi một khoảng trắng. Nếu trong danh sách ban đầu không có số lẻ nào, in ra -1.',
        'example_input': '5\n1 2 3 4 5',
        'example_output': '1 9 25',
        'explanation': 'Các số lẻ: 1, 3, 5. Bình phương: 1²=1, 3²=9, 5²=25.',
    },
    15: {
        'id': 15,
        'module_id': 'review_apr',
        'title': 'Sắp xếp từ khóa',
        'difficulty': 'Trung bình',
        'difficulty_color': '#facc15',
        'category': 'Lambda',
        'description': '''Cho một danh sách gồm N từ khóa (chỉ chứa các chữ cái tiếng Anh in thường). Hãy sắp xếp danh sách này theo tiêu chí sau:
<ul>
<li>Ưu tiên <strong>độ dài</strong> của từ khóa <strong>giảm dần</strong>.</li>
<li>Nếu độ dài bằng nhau, sắp xếp theo <strong>thứ tự từ điển tăng dần</strong> (A-Z).</li>
</ul>
<em>Lưu ý: Bắt buộc sử dụng hàm <code>sort()</code> hoặc <code>sorted()</code> kết hợp với tham số <code>key</code> là một hàm <code>lambda</code>.</em>''',
        'input_desc': 'Dòng đầu tiên chứa số nguyên N (1 ≤ N ≤ 1000). Dòng thứ hai chứa N từ khóa, cách nhau bởi khoảng trắng.',
        'output_desc': 'Danh sách các từ khóa sau khi sắp xếp, cách nhau bởi một khoảng trắng.',
        'example_input': '5\npython java c cpp ruby',
        'example_output': 'python java ruby cpp c',
        'explanation': '"python" (6 ký tự) dài nhất. "java" và "ruby" cùng 4 ký tự nhưng "java" đứng trước "ruby" theo từ điển.',
    },
    16: {
        'id': 16,
        'module_id': 'review_apr',
        'title': 'Xếp hạng học sinh',
        'difficulty': 'Khá',
        'difficulty_color': '#fb923c',
        'category': 'Lambda',
        'description': '''Có N học sinh tham gia kỳ thi. Thông tin mỗi học sinh gồm: Tên (viết liền không dấu), Điểm Toán và Điểm Văn. Hãy tính điểm trung bình của mỗi học sinh theo công thức <strong>(Toán + Văn) / 2</strong> và sắp xếp danh sách học sinh theo tiêu chí:
<ul>
<li>Điểm trung bình <strong>giảm dần</strong>.</li>
<li>Nếu điểm trung bình bằng nhau, sắp xếp theo Tên theo <strong>thứ tự từ điển tăng dần</strong> (A-Z).</li>
</ul>''',
        'input_desc': 'Dòng đầu chứa số nguyên dương N (1 ≤ N ≤ 100). N dòng tiếp theo, mỗi dòng chứa thông tin: Tên ĐiểmToán ĐiểmVăn (cách nhau bởi khoảng trắng). Điểm là số thực.',
        'output_desc': 'In ra tên của các học sinh sau khi đã sắp xếp, mỗi tên trên một dòng.',
        'example_input': '4\nAn 8.0 7.0\nBinh 9.0 9.0\nDung 7.5 7.5\nChi 9.5 8.5',
        'example_output': 'Binh\nChi\nAn\nDung',
        'explanation': 'Binh: TB=9.0, Chi: TB=9.0 (tên "Chi">"Binh" nên Binh trước), An: TB=7.5, Dung: TB=7.5 (An trước Dung theo A-Z).',
    },
    17: {
        'id': 17,
        'module_id': 'review_apr',
        'title': 'Thống kê từ vựng',
        'difficulty': 'Khá',
        'difficulty_color': '#fb923c',
        'category': 'Chuỗi',
        'description': '''Nhập vào một đoạn văn bản S. Hãy đếm tần suất xuất hiện của từng từ trong đoạn văn bản (<strong>không phân biệt hoa thường</strong>). Sau đó, in ra danh sách các từ và tần suất của chúng theo thứ tự:
<ul>
<li>Tần suất xuất hiện <strong>giảm dần</strong>.</li>
<li>Nếu tần suất bằng nhau, sắp xếp các từ theo <strong>thứ tự từ điển tăng dần</strong> (A-Z).</li>
</ul>''',
        'input_desc': 'Một dòng duy nhất chứa xâu ký tự S (S chỉ chứa chữ cái tiếng Anh và khoảng trắng, độ dài không quá 10⁴).',
        'output_desc': 'In ra mỗi từ và số lần xuất hiện của nó trên một dòng, cách nhau bởi một khoảng trắng.',
        'example_input': 'Python java PYTHON C C java python C',
        'example_output': 'c 3\npython 3\njava 2',
        'explanation': '"c" xuất hiện 3 lần (C, C, C), "python" xuất hiện 3 lần (Python, PYTHON, python), "java" xuất hiện 2 lần.',
    },
    18: {
        'id': 18,
        'module_id': 'review_apr',
        'title': 'Trích xuất và Tính toán',
        'difficulty': 'Nâng cao',
        'difficulty_color': '#f87171',
        'category': 'Lambda',
        'description': '''Cho N chuỗi biểu diễn thông tin kho hàng của các sản phẩm. Mỗi chuỗi có định dạng: <code>"MãSảnPhẩm-GiáTiền-SốLượng"</code>.
Hãy sử dụng kết hợp List Comprehension, <code>filter()</code>, <code>map()</code> và <code>lambda</code> để thực hiện các yêu cầu sau:
<ul>
<li>Chỉ giữ lại những sản phẩm có <strong>SốLượng > 0</strong>.</li>
<li>Tính tổng giá trị của từng sản phẩm hợp lệ (<strong>Tổng = GiáTiền × SốLượng</strong>).</li>
<li>Sắp xếp danh sách kết quả theo <strong>Tổng giá trị giảm dần</strong>, nếu bằng nhau thì ưu tiên <strong>MãSảnPhẩm theo thứ tự từ điển tăng dần</strong>.</li>
</ul>''',
        'input_desc': 'Dòng đầu chứa số nguyên dương N (1 ≤ N ≤ 1000). N dòng tiếp theo, mỗi dòng chứa chuỗi thông tin: MãSảnPhẩm-GiáTiền-SốLượng.',
        'output_desc': 'In ra MãSảnPhẩm và Tổng giá trị của các sản phẩm hợp lệ, mỗi sản phẩm trên một dòng, cách nhau một khoảng trắng.',
        'example_input': '4\nSP01-50-2\nSP02-100-0\nSP03-20-5\nSP04-30-4',
        'example_output': 'SP04 120\nSP01 100\nSP03 100',
        'explanation': 'SP02 bị loại (SL=0). SP04: 30×4=120, SP01: 50×2=100, SP03: 20×5=100. SP01 và SP03 bằng nhau, SP01 đứng trước theo A-Z.',
    },
}