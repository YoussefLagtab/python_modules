import sys

sys.tracebacklimit = 0

argv = sys.argv
argc = len(sys.argv)

if argc == 1:
    print()
    exit()
assert argc == 2, 'more than one argument is provided'
assert argv[1].isdigit(), 'argument is not integer'

number = int(argv[1])

if number == 0:
    print("I'm Zero.")
elif number % 2:
    print("I'm Odd.")
else:
    print("I'm Even.")
