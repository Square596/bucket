from argparse import ArgumentParser

def divination(petal, start):
    if sum(petal)%2 == 1:
        return start
    elif start == 'любит':
        return 'не любит'
    else:
        return 'любит'

if __name__ == '__main__':

    parser = ArgumentParser()

    parser.add_argument('-p', '--petal-numbers', required=True, nargs='*', type=int)
    parser.add_argument('-s', '--divination-start', required=False, type=str, default='любит', choices=['любит', 'не любит'])

    args = parser.parse_args()

    print(divination(args.petal_numbers, args.divination_start))
