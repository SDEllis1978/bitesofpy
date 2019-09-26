import os
import urllib.request
from string import ascii_letters

# PREWORK
DICTIONARY = os.path.join('/tmp, dictionary.txt')
urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)
scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}


def load_words():
    with open(DICTIONARY) as f:
        return [word.strip() for word in f.read().split()]


def calc_word_value(word):
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


def max_word_value(words=None):
    if words is None:
        words = load_words()
    return max(words, key=calc_word_value)
