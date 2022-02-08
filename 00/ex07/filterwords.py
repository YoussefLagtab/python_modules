import sys
from string import punctuation

if len(sys.argv) != 3 or not sys.argv[2].isnumeric():
    print('ERROR')
    exit(1)

length_accpeted = int(sys.argv[2])

text = sys.argv[1]
str = ''
for c in text:
    if c not in punctuation:
        str += c

print(list(filter(lambda e: len(e) > length_accpeted, str.split(' '))))
