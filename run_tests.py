# python run_tests.py          runs both parts
# python run_tests.py 1        runs only Part 1
# python run_tests.py 2        runs only Part 2
# python run_tests.py quick    runs both parts but skips program_10

import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

here = os.path.dirname(os.path.abspath(__file__))
part1_folder = os.path.join(here, "part1_program_cfg")
part2_folder = os.path.join(here, "part2_program_input_coverage")
part1_script = os.path.join(here, "part1.py")
part2_script = os.path.join(here, "part2.py")

choice = ""
if len(sys.argv) > 1:
    choice = sys.argv[1]

skip_program_10 = choice == "quick"
run_part1 = choice in ("", "1", "quick")
run_part2 = choice in ("", "2", "quick")

any_failed = False


def read_file(path):
    with open(path, "rb") as f:
        text = f.read().decode("utf-8", errors="replace")
    return text.replace("\r\n", "\n")


def print_summary(total, passed, failed):
    print("TOTAL: " + str(total))
    print("PASSED: " + str(passed))
    print("FAILED: " + str(failed))


# Part 1
if run_part1:
    print("Part 1")
    passed = 0
    failed = 0

    for filename in sorted(os.listdir(os.path.join(part1_folder, "programs"))):
        if not filename.endswith(".py"):
            continue
        if skip_program_10 and filename == "program_10.py":
            continue

        name = filename[:-3]
        program = os.path.join(part1_folder, "programs", filename)
        expected_file = os.path.join(part1_folder, "expected_cfgs", name + "_cfg.txt")

        result = subprocess.run([sys.executable, part1_script, program], capture_output=True)
        actual = result.stdout.decode("utf-8", errors="replace").replace("\r\n", "\n")
        expected = read_file(expected_file)

        if result.returncode == 0 and actual.strip() == expected.strip():
            print("PASS " + filename)
            passed += 1
        else:
            print("FAIL " + filename)
            failed += 1

    print_summary(passed + failed, passed, failed)
    if failed > 0:
        any_failed = True


# Part 2
def run_one_test(test):
    # returns True if the test passed
    name = test[0]
    input_name = test[1]
    program = os.path.join(part2_folder, "programs", name + ".py")
    input_file = os.path.join(part2_folder, "inputs", name, input_name + ".txt")
    expected_file = os.path.join(part2_folder, "expected_cov", name, input_name + "_cov.txt")

    try:
        result = subprocess.run([sys.executable, part2_script, program, input_file],
                                capture_output=True, timeout=120)
    except subprocess.TimeoutExpired:
        return False

    actual = result.stdout.decode("utf-8", errors="replace").replace("\r\n", "\n")
    return result.returncode == 0 and actual == read_file(expected_file)


if run_part2:
    print("Part 2")

    tests = []
    for filename in sorted(os.listdir(os.path.join(part2_folder, "programs"))):
        if not filename.endswith(".py"):
            continue
        if skip_program_10 and filename == "program_10.py":
            continue
        name = filename[:-3]
        for input_filename in sorted(os.listdir(os.path.join(part2_folder, "inputs", name))):
            if input_filename.endswith(".txt"):
                tests.append((name, input_filename[:-4]))

    # runs 16 tests at once so program_10 doesn't take hours
    with ThreadPoolExecutor(max_workers=16) as pool:
        results = list(pool.map(run_one_test, tests))

    passed = 0
    failed = 0
    for i in range(len(tests)):
        if results[i]:
            passed += 1
        else:
            failed += 1
            print("FAIL " + tests[i][0] + ".py / " + tests[i][1] + ".txt")

    print_summary(len(tests), passed, failed)
    if failed > 0:
        any_failed = True

if any_failed:
    sys.exit(1)