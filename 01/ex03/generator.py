from random import randint, sample


def sort_words(words):
    sorted_words = []

    for w in words:
        if len(sorted_words) == 0:
            sorted_words.append(w)
            continue
        for i, ww in enumerate(sorted_words):
            if w < ww:
                sorted_words.insert(i, w)
                break
            elif i == len(sorted_words) - 1:
                sorted_words.append(w)
                break

    return sorted_words


def shuffle_words(words):
    shuffled_words = []
    for w in words:
        i = randint(0, len(words))
        shuffled_words.insert(i, w)

    return shuffled_words


def get_unique_words(words):
    unique_words = []
    for w in words:
        if w not in unique_words:
            unique_words.append(w)

    return unique_words


def generator(text, sep=" ", option=None):
    try:
        words = text.split(sep)

        if option == "shuffle":
            words = shuffle_words(words)
        elif option == "unique":
            words = get_unique_words(words)
        elif option == "ordered":
            words = sort_words(words)
        elif option:
            return Exception()
    except Exception:
        yield "ERROR"
        return

    for w in words:
        yield w
