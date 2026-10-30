# Part 2: print the statement coverage of a Python program
# python part2.py <program.py> <input.txt>

import ctypes
import os
import runpy
import sys
import threading

import coverage

program_path = os.path.abspath(sys.argv[1])
input_path = sys.argv[2]

# the words in the input file are the arguments
with open(input_path, encoding="utf-8") as f:
    arguments = f.read().split()

with open(program_path, encoding="utf-8") as f:
    source_lines = f.read().split("\n")

# remove the empty last line
if source_lines[-1] == "":
    source_lines.pop()

cov = coverage.Coverage(data_file=None, include=[program_path])

sys.argv = [program_path] + arguments
sys.path.insert(0, os.path.dirname(program_path))

# hide what the program prints
real_stdout = sys.stdout
sys.stdout = open(os.devnull, "w")


class TimeUp(BaseException):
    pass


main_thread = threading.get_ident()


# stops the program after 60 seconds
def stop_program():
    ctypes.pythonapi.PyThreadState_SetAsyncExc(
        ctypes.c_ulong(main_thread), ctypes.py_object(TimeUp)
    )


timer = threading.Timer(60, stop_program)
timer.daemon = True
timer.start()

# run the program with coverage on
cov.start()
try:
    runpy.run_path(program_path, run_name="__main__")
except BaseException:
    pass

timer.cancel()
cov.stop()
sys.stdout.close()
sys.stdout = real_stdout

result = cov.analysis2(program_path)
all_statements = result[1]
missing_lines = result[3]

output = []
line_number = 1
for line in source_lines:
    # checks if the line was run
    if line_number in all_statements and line_number not in missing_lines:
        prefix = "  "
    else:
        prefix = "# "
    number = str(line_number).rjust(4)
    output.append(prefix + number + ": " + line.rstrip())
    line_number += 1

sys.stdout.buffer.write(("\n".join(output) + "\n").encode("utf-8"))