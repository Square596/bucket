from argparse import ArgumentParser
import re


def drop(string):
    for match in re.finditer(r'(\b\w*?)д(\w*?)н(\w*?)к(\w*?\b)', string):
        for delete_group in map(match.span, range(1, 5)):
            string = string[:delete_group[0]] + ' '*(delete_group[1] - delete_group[0]) + string[delete_group[1]:] #ничего умнее не придумал ;(

    return string


def open_txt(path):
    with open(path, encoding='utf-8') as file:
        return ''.join(file.readlines())


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('path', type=str)
    args = parser.parse_args()

    print(drop(open_txt(args.path)))