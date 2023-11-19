from data.letters import *


def ru_to_arm(line: str, letters=FIRST_SET) -> str:
    out_list = []
    for c in line:
        if c in letters:
            out_list.append(letters[c])
        else:
            out_list.append(c)
    # print(out_list)
    s = ''.join(out_list)
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
    convert_file('leskov-rasskazy.txt', BGDP)


