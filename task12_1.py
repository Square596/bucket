from argparse import ArgumentParser
import re


def search_money(string):
    return re.finditer(r'((\d+)(\s?)(\$|₽|€))|((\$|₽|€)(\s?)(\d+))', string)


def open_txt(path):
    with open(path, encoding='utf-8') as file:
        return ''.join(file.readlines())


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('path', type=str)
    args = parser.parse_args()

    money = []
    for match in search_money(open_txt(args.path)):
        if match.group(2) is None:
            money.append(match.group(8))
        else:
            money.append(match.group(2))
    print(money)