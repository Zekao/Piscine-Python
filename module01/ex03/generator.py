import random

def generator(text, sep=" ", option=None):
    """Splits the text according to sep value and yield the substrings.
    option precise if a action is performed to the substrings before it is yielded."""

    assert isinstance(text, str), "ERROR"
    assert isinstance(sep, str), "ERROR"
    assert option in [None, "shuffle", "unique", "ordered"], "ERROR"

    words = text.split(sep)

    if option == "shuffle":
        words =  [words.pop(random.randrange(len(words))) for _ in range(len(words))]

    elif option == "unique":
        words = list(set(words))

    elif option == "ordered":
        words = sorted(words)
    for word in words:
        yield word


