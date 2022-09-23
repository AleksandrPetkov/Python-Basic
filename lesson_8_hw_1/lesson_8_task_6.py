"""
Function 'pemrtuate' take the user text and permute the letters in words,
but only between first and last letter of the word.
"""

import random


def pemrtuate(text):
    text_final = []
    text = text.split()
    for words in text:
        if len(words) <= 3:
            text_final.append(words)
        else:
            words_list = []
            for symbol in words:
                words_list.append(symbol)
            first_symbol = words_list[0]
            last_symbol = words_list[-1]
            del words_list[0]
            del words_list[-1]
            while True:
                if len(words_list) <= 2:
                    random.shuffle(words_list)
                    words_list = ''.join(words_list)
                    break
                else:
                    word_part = words_list[0:3]
                    del words_list[0:3]
                    random.shuffle(word_part)
                    first_symbol += ''.join(word_part)

            ok_text = first_symbol + words_list + last_symbol
            text_final.append(ok_text)
    result = ' '.join(text_final)
    return result


def main():
    user_text = 'Потьомкінські сходи — відомі сходи в Одесі, що поєднують центр міста з гаванню та Морським вокзалом.'
    print('Original text is: ', user_text)
    print('Changed text is: ', pemrtuate(user_text))


main()
