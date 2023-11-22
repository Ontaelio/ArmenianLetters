from data.letters import *


def check_special_cases(word: str, letters: dict) -> str:
    if 'ев' in letters.keys():
        word = word.replace('ев', letters['ев'])

    if 'Во' in letters.keys():
        if word.upper().startswith('ВО'):
            word = letters[word[:2]] + word[2:]

    if 'О+' in letters.keys():
        if word.upper().startswith('О'):
            word = letters[word[0]+'+'] + word[1:]

    if 'дз' in letters.keys():
        word = word.replace('дз', letters['дз'])
        word = word.replace('ДЗ', letters['ДЗ'])
        word = word.replace('Дз', letters['Дз'])

    if 'ть' in letters.keys():
        word = word.replace('ть', letters['ть'])
        word = word.replace('ти', letters['ть'] + 'и')
        word = word.replace('те', letters['ть'] + 'е')
        word = word.replace('тё', letters['ть'] + 'ё')
        word = word.replace('тя', letters['ть'] + 'я')
        word = word.replace('тю', letters['ть'] + 'ю')
        word = word.replace('Ть', letters['ТЬ'])
        word = word.replace('Ти', letters['ТЬ'] + 'и')
        word = word.replace('Те', letters['ТЬ'] + 'е')
        word = word.replace('Тё', letters['ТЬ'] + 'ё')
        word = word.replace('Тя', letters['ТЬ'] + 'я')
        word = word.replace('Тю', letters['ТЬ'] + 'ю')
        word = word.replace('ТЬ', letters['ТЬ'])
        word = word.replace('ТИ', letters['ТЬ'] + 'И')
        word = word.replace('ТЕ', letters['ТЬ'] + 'Е')
        word = word.replace('ТЁ', letters['ТЬ'] + 'Ё')
        word = word.replace('ТЯ', letters['ТЬ'] + 'Я')
        word = word.replace('ТЮ', letters['ТЬ'] + 'Ю')

    if 'дж' in letters.keys():
        word = word.replace('дж', letters['дж'])
        word = word.replace('ДЖ', letters['ДЖ'])
        word = word.replace('Дж', letters['Дж'])

    if 'рь' in letters.keys():
        word = word.replace('рь', letters['рь'])
        word = word.replace('ри', letters['рь'] + 'и')
        word = word.replace('ре', letters['рь'] + 'е')
        word = word.replace('рё', letters['рь'] + 'ё')
        word = word.replace('ря', letters['рь'] + 'я')
        word = word.replace('рю', letters['рь'] + 'ю')
        word = word.replace('Рь', letters['РЬ'])
        word = word.replace('Ри', letters['РЬ'] + 'и')
        word = word.replace('Ре', letters['РЬ'] + 'е')
        word = word.replace('Рё', letters['РЬ'] + 'ё')
        word = word.replace('Ря', letters['РЬ'] + 'я')
        word = word.replace('Рю', letters['РЬ'] + 'ю')
        word = word.replace('РЬ', letters['РЬ'])
        word = word.replace('РИ', letters['РЬ'] + 'И')
        word = word.replace('РЕ', letters['РЬ'] + 'Е')
        word = word.replace('РЁ', letters['РЬ'] + 'Ё')
        word = word.replace('РЯ', letters['РЬ'] + 'Я')
        word = word.replace('РЮ', letters['РЬ'] + 'Ю')

    return word


def ru_to_arm(line: str, letters) -> str:
    out_words = []
    words = line.split(' ')

    for word in words:
        word = check_special_cases(word, letters)

        out_list = []
        for c in word:
            if c in letters:
                out_list.append(letters[c])
            else:
                out_list.append(c)
        out_words.append(''.join(out_list))
    s = ' '.join(out_words)
    return s


def convert_file(filename, letters):
    filename = 'texts/' + filename
    with open(filename, 'r', encoding="utf-8") as fin:
        with open(filename.split('.')[0] + '_arm.' + filename.split('.')[1], 'w', encoding="utf-8") as fout:
            for ru_line in fin:
                if (ord(ru_line[0]) == 10):
                    ru_line = fin.readline()
                # ru_line = fin.readline()

                fout.write(ru_to_arm(ru_line, letters))
    # ru

    # fin.write(ru_txt)


if __name__ == '__main__':
    # s = input(': ')
    # print(ru_to_arm(s))
    # rus_to_arm('onegin.txt')
    # print(FIRST_SET)
    convert_file('leskov_drovokol.txt',  CONSONANTS_BOTH_RS)


