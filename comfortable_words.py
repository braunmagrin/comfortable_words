# coding: utf-8

import re
from random import choice


def valid_word(word, min_len=2):
    if len(word) < min_len or re.search('[^qwertasdfgzxcvbyuiophjklnm]', word):
        return False

    new = re.subn('[qwertasdfgzxcvb]', ' ', word)[0]
    return re.search('\s{2}|\w{2}', new) is None


words_file = open('/usr/share/dict/words', 'r')
words = words_file.read().splitlines()
all_valid_words = list(filter(valid_word, words))


if __name__ == '__main__':
    liked = False
    while(not liked):
        print(choice(all_valid_words))
        answer = input('Did you like this word? [y/n]  ')
        liked = answer.lower() == 'y'
