'''Unit tests for calc app'''
import pytest
import calc

test_word_array = ['DoG', ' CAT', '   mOnKeY    ']
def test_standardize_word():
    assert calc.standardize_word(test_word_array[0]) == 'dog'
    assert calc.standardize_word(test_word_array[1]) == 'cat'
    assert calc.standardize_word(test_word_array[2]) == 'monkey'
