import sys


def is_alpha_or_space(text):
    return all(c.isalnum() or c.isspace() for c in text)


if len(sys.argv) < 2 or not is_alpha_or_space(' '.join(sys.argv[1::])):
    print('ERROR')
    exit(1)

text = ' '.join(sys.argv[1::])
morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----'}

is_first = 1
for c in text:
    if not is_first:
        print(' ', end='')
    is_first = 0

    if c.isalnum():
        print(morse_dict[c.upper()], end='')
    else:
        print('/', end='')
print()
