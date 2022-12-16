from threading import Thread
from argparse import ArgumentParser
import os


def search(path, name, string):
    output = ''
    with open(os.path.join(path, name), 'r') as file:
        for line in file:
            if string in line:
                output += f'{name}: {line}'
        print(output[:-2]) # delete \n at the last line


def separate_txt_iterable(path, string):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            if os.path.splitext(file)[1] == '.txt':
                yield (path, file, string, ) # this format is specifically for Thread  


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('string', type=str)
    parser.add_argument('path', type=str)
    args = parser.parse_args()

    threads = [Thread(target=search, args=i) for i in separate_txt_iterable(args.path, args.string)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
