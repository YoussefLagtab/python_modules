from string import punctuation, whitespace
import sys

sys.tracebacklimit = 0


def text_analyzer(*args):
    """This function counts the number of upper characters, lower characters,
punctuation and spaces in a given text."""

    argc = len(args)
    if argc > 1 or (argc == 1 and not isinstance(args[0], str)):
        print('ERROR')
        return

    if argc == 0:
        text = input('enter your text:\n')
    else:
        text = args[0]
    if not text:
        text = "Ab, "
        print(f'text is empty, using default value: |{text}|')

    number_of_lower_chars = 0
    number_of_upper_chars = 0
    number_of_punctuation = 0
    number_of_spaces = 0
    for c in text:
        if c.islower():
            number_of_lower_chars += 1
        elif c.isupper():
            number_of_upper_chars += 1
        elif c in whitespace:
            number_of_spaces += 1
        elif c in punctuation:
            number_of_punctuation += 1

    print('The text contains', len(text), 'characters:')
    print('-', number_of_upper_chars, "upper letters")
    print('-', number_of_lower_chars, "lower letters")
    print('-', number_of_punctuation, "punctuation marks")
    print('-', number_of_spaces, "spaces")
