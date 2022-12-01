from multiprocessing import Pool
from argparse import ArgumentParser
import os


def search(path, name, string):
    with open(os.path.join(path, name), 'r') as file:
        output = ''
        while True:
            line = file.readline()
            if not line:
                print(output[:-2]) #del "\n"
                break
            if string in line:
                output += f'{name}: {line}'


def separate_txt_iterable(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            if os.path.splitext(file)[1] == '.txt':
                yield file


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('string', type=str)
    parser.add_argument('path', type=str)
    args = parser.parse_args()

    pool = Pool()
    for x in separate_txt_iterable(args.path):
        pool.apply(search, args=(args.path, x, args.string))