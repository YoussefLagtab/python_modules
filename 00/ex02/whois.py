import sys

args = sys.argv
if len(args) > 2 or not args[1].isnumeric():
    print('ERROR')
    sys.exit(1)

number = int(args[1])
if number % 2:
    print("I'm Odd.")
else:
    print("I'm Even.")
