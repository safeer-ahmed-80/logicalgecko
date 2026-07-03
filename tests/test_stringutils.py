import unittest

from src.stringutils import reverse_words, is_palindrome


class TestReverseWords(unittest.TestCase):
    def test_reverses_multiple_words(self):
        self.assertEqual(reverse_words("hello world"), "world hello")

    def test_single_word_unchanged(self):
        self.assertEqual(reverse_words("hello"), "hello")


class TestIsPalindrome(unittest.TestCase):
    def test_simple_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))

    def test_non_palindrome(self):
        self.assertFalse(is_palindrome("hello"))

    def test_ignores_case_and_spaces(self):
        self.assertTrue(is_palindrome("Race car"))


if __name__ == "__main__":
    unittest.main()
