from data.letters import *


def special_left_strip(word: str) -> (str, str):
    t = ''
    while word[0] in ["'", '"', '“', '«', '\n', '\r', '\t', '\f']:
        t = t + word[0]
        word = word[1:]

    return t, word


def check_special_cases(word: str, letters: dict) -> str:
    if not word:
        return word

    if 'ев' in letters.keys():
        word = word.replace('ев', letters['ев'])

    if 'Во' in letters.keys():
        if word[0] in ["'", '"', '“', '«', '\n', '\r', '\t', '\f']:
            t, w = special_left_strip(word)
            if w.upper().startswith('ВО'):
                word = t + letters[w[:2]] + w[2:]
        elif word.upper().startswith('ВО'):
            word = letters[word[:2]] + word[2:]

    if 'О+' in letters.keys():
        if word[0] in ["'", '"', '“', '«', '\n', '\r', '\t', '\f']:
            t, w = special_left_strip(word)
            if w.upper().startswith('О'):
                word = t + letters[w[0] + '+'] + w[1:]
        elif word.upper().startswith('О'):
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

    if 'тъ' in letters.keys():
        word = word.replace('та', letters['тъ'] + 'а')
        word = word.replace('тэ', letters['тъ'] + 'э')
        word = word.replace('то', letters['тъ'] + 'о')
        word = word.replace('ту', letters['тъ'] + 'у')
        word = word.replace('ты', letters['тъ'] + 'ы')
        word = word.replace('ти', letters['тъ'] + 'и')
        word = word.replace('те', letters['тъ'] + 'е')
        word = word.replace('тё', letters['тъ'] + 'ё')
        word = word.replace('тю', letters['тъ'] + 'ю')
        word = word.replace('тя', letters['тъ'] + 'я')
        word = word.replace('Та', letters['ТЪ'] + 'а')
        word = word.replace('Тэ', letters['ТЪ'] + 'э')
        word = word.replace('То', letters['ТЪ'] + 'о')
        word = word.replace('Ту', letters['ТЪ'] + 'у')
        word = word.replace('Ты', letters['ТЪ'] + 'ы')
        word = word.replace('Ти', letters['ТЪ'] + 'и')
        word = word.replace('Те', letters['ТЪ'] + 'е')
        word = word.replace('Тё', letters['ТЪ'] + 'ё')
        word = word.replace('Тя', letters['ТЪ'] + 'я')
        word = word.replace('Тю', letters['ТЪ'] + 'ю')
        word = word.replace('ТА', letters['ТЪ'] + 'А')
        word = word.replace('ТЭ', letters['ТЪ'] + 'Э')
        word = word.replace('ТО', letters['ТЪ'] + 'О')
        word = word.replace('ТУ', letters['ТЪ'] + 'У')
        word = word.replace('ТЫ', letters['ТЪ'] + 'Ы')
        word = word.replace('ТИ', letters['ТЪ'] + 'И')
        word = word.replace('ТЕ', letters['ТЪ'] + 'Е')
        word = word.replace('ТЁ', letters['ТЪ'] + 'Ё')
        word = word.replace('ТЯ', letters['ТЪ'] + 'Я')
        word = word.replace('ТЮ', letters['ТЪ'] + 'Ю')
        
    if 'къ' in letters.keys():
        word = word.replace('ка', letters['къ'] + 'а')
        word = word.replace('кэ', letters['къ'] + 'э')
        word = word.replace('ко', letters['къ'] + 'о')
        word = word.replace('ку', letters['къ'] + 'у')
        word = word.replace('кы', letters['къ'] + 'ы')
        word = word.replace('ки', letters['къ'] + 'и')
        word = word.replace('ке', letters['къ'] + 'е')
        word = word.replace('кё', letters['къ'] + 'ё')
        word = word.replace('кю', letters['къ'] + 'ю')
        word = word.replace('кя', letters['къ'] + 'я')
        word = word.replace('Ка', letters['КЪ'] + 'а')
        word = word.replace('Кэ', letters['КЪ'] + 'э')
        word = word.replace('Ко', letters['КЪ'] + 'о')
        word = word.replace('Ку', letters['КЪ'] + 'у')
        word = word.replace('Кы', letters['КЪ'] + 'ы')
        word = word.replace('Ки', letters['КЪ'] + 'и')
        word = word.replace('Ке', letters['КЪ'] + 'е')
        word = word.replace('Кё', letters['КЪ'] + 'ё')
        word = word.replace('Кя', letters['КЪ'] + 'я')
        word = word.replace('Кю', letters['КЪ'] + 'ю')
        word = word.replace('КА', letters['КЪ'] + 'А')
        word = word.replace('КЭ', letters['КЪ'] + 'Э')
        word = word.replace('КО', letters['КЪ'] + 'О')
        word = word.replace('КУ', letters['КЪ'] + 'У')
        word = word.replace('КЫ', letters['КЪ'] + 'Ы')
        word = word.replace('КИ', letters['КЪ'] + 'И')
        word = word.replace('КЕ', letters['КЪ'] + 'Е')
        word = word.replace('КЁ', letters['КЪ'] + 'Ё')
        word = word.replace('КЯ', letters['КЪ'] + 'Я')
        word = word.replace('КЮ', letters['КЪ'] + 'Ю')
        
    if 'пъ' in letters.keys():
        word = word.replace('па', letters['пъ'] + 'а')
        word = word.replace('пэ', letters['пъ'] + 'э')
        word = word.replace('по', letters['пъ'] + 'о')
        word = word.replace('пу', letters['пъ'] + 'у')
        word = word.replace('пы', letters['пъ'] + 'ы')
        word = word.replace('пи', letters['пъ'] + 'и')
        word = word.replace('пе', letters['пъ'] + 'е')
        word = word.replace('пё', letters['пъ'] + 'ё')
        word = word.replace('пю', letters['пъ'] + 'ю')
        word = word.replace('пя', letters['пъ'] + 'я')
        word = word.replace('Па', letters['ПЪ'] + 'а')
        word = word.replace('Пэ', letters['ПЪ'] + 'э')
        word = word.replace('По', letters['ПЪ'] + 'о')
        word = word.replace('Пу', letters['ПЪ'] + 'у')
        word = word.replace('Пы', letters['ПЪ'] + 'ы')
        word = word.replace('Пи', letters['ПЪ'] + 'и')
        word = word.replace('Пе', letters['ПЪ'] + 'е')
        word = word.replace('Пё', letters['ПЪ'] + 'ё')
        word = word.replace('Пя', letters['ПЪ'] + 'я')
        word = word.replace('Пю', letters['ПЪ'] + 'ю')
        word = word.replace('ПА', letters['ПЪ'] + 'А')
        word = word.replace('ПЭ', letters['ПЪ'] + 'Э')
        word = word.replace('ПО', letters['ПЪ'] + 'О')
        word = word.replace('ПУ', letters['ПЪ'] + 'У')
        word = word.replace('ПЫ', letters['ПЪ'] + 'Ы')
        word = word.replace('ПИ', letters['ПЪ'] + 'И')
        word = word.replace('ПЕ', letters['ПЪ'] + 'Е')
        word = word.replace('ПЁ', letters['ПЪ'] + 'Ё')
        word = word.replace('ПЯ', letters['ПЪ'] + 'Я')
        word = word.replace('ПЮ', letters['ПЪ'] + 'Ю')

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


def ru_to_arm(text: str, letters) -> str:
    out_lines = []
    lines = text.split('\n')  # line feed split, needed for special cases in web interface

    for line in lines:
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
        out_lines.append(s)

    return "\n".join(out_lines)


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


