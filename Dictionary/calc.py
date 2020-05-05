'''Creates a user dictionary that returns the definition of a word'''
import json
import sys

def standardize_word(input_word):
    clean_word = input_word.lower().strip()
    return clean_word

def translate(word, dictionary):
    '''sanitizes input, takes in dictionary and returns definition'''
    clean_word = word.lower()
    return dictionary[clean_word]

def main():
    '''runs main logic for app'''
    data = json.load(open('data.json'))
    user_word = input('Enter word: ')
    print(translate(user_word, data))
    sys.exit()
    