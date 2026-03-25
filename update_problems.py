import re

with open('problems.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Add MODULES at the top
modules_def = """MODULES = {
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
    }
}

"""

if 'MODULES =' not in text:
    text = text.replace('PROBLEMS = {', modules_def + 'PROBLEMS = {')

# Add module_id to each existing problem
for i in range(1, 11):
    search = f"    {i}: {{\n        'id': {i},"
    replace = f"    {i}: {{\n        'id': {i},\n        'module_id': 'lambda',"
    if replace not in text:
        text = text.replace(search, replace)

# Add dummy problems to basics
dummy_problems = """
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
"""

if 'id\': 11,' not in text:
    # insert before the last }
    text = text.rsplit('}', 1)[0] + dummy_problems + '}'

with open('problems.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("problems.py updated successfully.")
