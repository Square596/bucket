import random
from typing import List, Optional
from argparse import ArgumentParser


class RandomChoiceIterator:

    def __init__(self, values: List[int], num_iters: Optional[int] = None, seed: Optional[int|float] = None):
        if not values:
            raise ValueError('List of values is empty! It must contain at least one value!')
        self.values = values
        self.num_iters = num_iters
        random.seed(seed)
        if self.num_iters is not None:
            self.current_iteration = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.num_iters is None:
            return random.choice(self.values)
        elif self.current_iteration >= self.num_iters:
            raise StopIteration()
        else:
            self.current_iteration += 1
            return random.choice(self.values)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-v', '--values', required=True, nargs='*', type=int)
    parser.add_argument('-n', '--num-iters', required=False, type=int, default=None)
    parser.add_argument('-s', '--seed', required=False, type=float, default=None)
    args = parser.parse_args()

    for value in RandomChoiceIterator(values=args.values, num_iters=args.num_iters, seed=args.seed):
        print(value)
