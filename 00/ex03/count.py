from string import punctuation, whitespace

def text_analyzer(text = ''):
    "This function counts the number of upper characters, lower characters, punctuation and spaces in a given text."

    if len(locals()) > 1 or not isinstance(text, str):
        print('ERROR')
        return

    if not text:
        text = input('enter your text:\n')

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

text_analyzer(2)