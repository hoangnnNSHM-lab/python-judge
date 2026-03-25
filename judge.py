import subprocess
import os
import json
import tempfile

TESTCASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'testcases')
TIMEOUT = 5  # seconds


def judge_submission(problem_id, code):
    """
    Run student code against all test cases for a problem.
    Returns dict with 'score', 'total', 'details' (list of per-test results).
    """
    tc_dir = os.path.join(TESTCASE_DIR, f"problem_{problem_id:02d}")
    if not os.path.isdir(tc_dir):
        return {'score': 0, 'total': 100, 'details': [], 'error': 'Problem not found'}

    # Find all test cases
    test_files = sorted([f for f in os.listdir(tc_dir) if f.startswith('input_')])
    details = []
    total_score = 0
    points_per_test = 10

    for tf in test_files:
        tc_num = tf.replace('input_', '').replace('.txt', '')
        input_file = os.path.join(tc_dir, f"input_{tc_num}.txt")
        output_file = os.path.join(tc_dir, f"output_{tc_num}.txt")

        if not os.path.exists(output_file):
            continue

        with open(input_file, 'r') as f:
            input_data = f.read()
        with open(output_file, 'r') as f:
            expected_output = f.read().strip()

        result = run_code(code, input_data)

        if result['status'] == 'ok':
            actual = result['output'].strip()
            passed = actual == expected_output
            if passed:
                total_score += points_per_test
            details.append({
                'test': int(tc_num),
                'passed': passed,
                'points': points_per_test if passed else 0,
                'status': 'AC' if passed else 'WA',
                'expected': expected_output[:200],
                'actual': actual[:200],
            })
        elif result['status'] == 'timeout':
            details.append({
                'test': int(tc_num),
                'passed': False,
                'points': 0,
                'status': 'TLE',
                'expected': expected_output[:200],
                'actual': 'Time Limit Exceeded',
            })
        else:
            details.append({
                'test': int(tc_num),
                'passed': False,
                'points': 0,
                'status': 'RE',
                'expected': expected_output[:200],
                'actual': result.get('error', 'Runtime Error')[:200],
            })

    return {
        'score': total_score,
        'total': len(details) * points_per_test,
        'details': details,
    }


def run_code(code, input_data):
    """Run Python code with given input, return output or error."""
    # Write code to temp file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as tmp:
        tmp.write(code)
        tmp_path = tmp.name

    try:
        proc = subprocess.run(
            ['python3', tmp_path],
            input=input_data,
            capture_output=True,
            text=True,
            timeout=TIMEOUT,
        )
        if proc.returncode != 0:
            return {'status': 'error', 'error': proc.stderr[:500]}
        return {'status': 'ok', 'output': proc.stdout}
    except subprocess.TimeoutExpired:
        return {'status': 'timeout'}
    except Exception as e:
        return {'status': 'error', 'error': str(e)}
    finally:
        try:
            os.unlink(tmp_path)
        except:
            pass
