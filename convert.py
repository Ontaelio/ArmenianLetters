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

    return word


def ru_to_arm(line: str, letters=FIRST_SET) -> str:
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


def convert_file(filename, letters=FIRST_SET):
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
    convert_file('leskov_drovokol.txt',  LESSON_4)


