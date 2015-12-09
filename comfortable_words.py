# coding: utf-8

import itertools
from random import choice

lhs_letters = 'qwertasdfgzxcvb'
rhs_letters = 'yuiophjklçnm'

words_file = open('/usr/share/dict/words', 'r')
words = words_file.read().splitlines()


def valid_pair(pair):
    return (((pair[0] in lhs_letters) and (pair[1] in rhs_letters)) or
            ((pair[0] in rhs_letters) and (pair[1] in lhs_letters)))


def valid_word(word, rec=False, min_len=2):
    if not rec and len(word) < min_len:
        return False
    elif rec and len(word) < 2:
        return True

    return valid_pair(word[:2]) and valid_word(word[1:], rec=True)


all_valid_words = list(filter(valid_word, words))


if __name__ == '__main__':
    liked = False
    while(not liked):
        print(choice(all_valid_words))
        answer = input('Did you like this word? [y/n]  ')
        liked = answer.lower() == 'y'
