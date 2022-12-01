from threading import Thread, current_thread
from argparse import ArgumentParser
import time


def factorize(number):
    out_number = number
    global watch
    watch[current_thread().name] = time.time()

    Ans = []
    d = 2
    while d * d <= number:
        if number % d == 0:
            Ans.append(d)
            number //= d
        else:
            d += 1
    if number > 1:
        Ans.append(number)
    
    while True:
        if watch[current_thread().name] == min(watch.values()):
            print(f'{out_number}: ', end='')
            print(*Ans)
            watch.pop(current_thread().name)
            break


def launch_threads(list_numbers):
    threads = [Thread(target=factorize, args=(i,)) for i in list_numbers]
    for thread in threads:
        thread.start()


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('values', type=int, nargs='*')
    args = parser.parse_args()
    watch = {}
    launch_threads(args.values)
