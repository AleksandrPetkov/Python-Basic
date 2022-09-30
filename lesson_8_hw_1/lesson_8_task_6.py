"""
Function 'pemrtuate' take the user text and permute the letters in words,
but only between first and last letter of the word.
"""

import random
from copy import deepcopy
from string import punctuation


def pemrtuate(text):
    text_final = []
    text_list = text.split()
    for words in text_list:
        if len(words) <= 3:
            text_final.append(words)
        else:
            punctuation_list = [letter for letter in words[-1] if letter in punctuation]
            words_list = [letter for letter in words if letter not in punctuation]
            first_part = [x for x in words_list[0]]
            last_part = [x for x in words_list[-1]]
            work_word_part = [element for element in words_list[1:-1]]
            while True:
                if len(work_word_part) == 0 or len(work_word_part) == 1:
                    first_part += work_word_part
                    break
                elif len(work_word_part) == 2:
                    work_word_part[0], work_word_part[1] = work_word_part[1], work_word_part[0]
                    first_part += work_word_part
                    break
                else:
                    mid_part = [work_word_part.pop(0) for _ in range(3)]
                    word_part_copy = deepcopy(mid_part)
                    while mid_part == word_part_copy:
                        random.shuffle(mid_part)
                    first_part += mid_part
            ok_text = ''.join(first_part + last_part + punctuation_list)
            text_final.append(ok_text)
    result = ' '.join(text_final)
    return result


def main():
    user_text = 'Потьомкінські сходи — відомі сходи в Одесі, що поєднують центр міста з гаванню та Морським вокзалом.'
    print('Original text is: ', user_text)
    print('Changed text is: ', pemrtuate(user_text))


if __name__ == '__main__':
    main()
