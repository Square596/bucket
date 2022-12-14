from multiprocessing import Pool
from argparse import ArgumentParser


def factorize(number):
    out_number = number
    ans = []
    d = 2
    while d * d <= number:
        if number % d == 0:
            ans.append(d)
            number //= d
        else:
            d += 1
    if number > 1:
        ans.append(number)
    
    return f'{out_number}: ' + ' '.join(map(str, ans))


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('values', type=int, nargs='*')
    args = parser.parse_args()

    pool = Pool()
    print('\n'.join(pool.map(factorize, args.values)))
