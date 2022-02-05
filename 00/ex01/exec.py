import sys

args = ' '.join(sys.argv[1:])

results = ''
for c in args:
    if c.islower():
        results = c.upper() + results
    else:
        results = c.lower() + results

print(results)
