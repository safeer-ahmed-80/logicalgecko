# logicalgecko

A tiny collection of string utility functions, written while learning how to ship
changes with Claude Code.

## Functions

- `reverse_words(text)` — reverses the order of words in a sentence.
- `is_palindrome(text)` — checks whether a string reads the same forwards and
  backwards, ignoring case and spaces.

## Usage

```python
from src.stringutils import reverse_words, is_palindrome

reverse_words("hello world")   # "world hello"
is_palindrome("Race car")      # True
```

## Running tests

```bash
python -m unittest discover tests
```
