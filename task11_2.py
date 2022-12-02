from multiprocessing import Pool
from argparse import ArgumentParser
import os


def search(path, name, string):
    output = ''
    with open(os.path.join(path, name), 'r') as file:
        while True:
            line = file.readline()
            if not line:
                return output
            if string in line:
                output += f'{name}: {line}'


def separate_txt_iterable(path, string):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            if os.path.splitext(file)[1] == '.txt':
                yield path, file, string


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('string', type=str)
    parser.add_argument('path', type=str)
    args = parser.parse_args()

    pool = Pool()
    print(''.join(pool.starmap(search, separate_txt_iterable(args.path, args.string))))
