from contextlib import redirect_stdout
from io import StringIO

EXPECTED_OUTPUT = """# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # #
# # #
# # #"""

f = StringIO()
with redirect_stdout(f):
    cases = int(input().rstrip())
    for i in range(cases):
        line = int(input().rstrip())
        for j in range(line):
            current_line = ""
            for k in range(line):
                current_line += "# "
            print(current_line.rstrip())
s = f.getvalue().strip()
print(s)
