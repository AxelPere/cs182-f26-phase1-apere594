# CS 182 Project Phase 1

## Project Structure
- `part1.py`: Prints the control flow graph (CFG) of a Python program using `py2cfg`.
- `part2.py`: Prints the statement coverage of a Python program using `coverage`.
- `run_tests.py`: Runs all the tests and compares the output with the expected output.
- `requirements.txt`: Required packages.
- `part1_program_cfg/`: Part 1 programs and expected CFG outputs.
- `part2_program_input_coverage/`: Part 2 programs, inputs, and expected coverage outputs.
- `.github/workflows/`: GitHub Actions workflow that runs the tests on every push.

## Setup
```bash
pip install -r requirements.txt
```

## How to Run

### Part 1
```bash
python part1.py path/to/program.py
```
Prints the number of nodes, each node (ID, line numbers, source code), the number of edges, and each edge (source, target, and condition if it has one).

### Part 2
```bash
python part2.py path/to/program.py path/to/input.txt
```
Runs the program with the input and prints each line of the program. A line starts with `# ` if it was not run, or two spaces if it was run. A program that runs longer than 1 minute is stopped.

## How to Run the Tests
```bash
python run_tests.py
```
Other options:
```bash
python run_tests.py 1       # only Part 1
python run_tests.py 2       # only Part 2
python run_tests.py quick   # both parts, skips program_10
```
Each part prints the total, passed, and failed counts. Failed tests are listed by program name (and input name for Part 2).