def reverse_words(text):
    """Reverse the order of words in a sentence."""
    return " ".join(text.split()[::-1])


def is_palindrome(text):
    """Check whether text reads the same forwards and backwards.

    Ignores case and spaces.
    """
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]
