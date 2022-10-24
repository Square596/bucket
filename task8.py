import random
from typing import List, Optional


class RandomChoiceIterator:

    def __init__(self, values: List[int], num_iters: Optional[int] = None):
        self.values = values
        self.num_iters = num_iters
        if self.num_iters:
            self.current_iteration = 0

    def __next__(self):
        if not self.num_iters:
            return random.choice(self.values)
        elif self.current_iteration >= self.num_iters:
            raise StopIteration()
        else:
            self.current_iteration += 1
            return random.choice(self.values)

    def __iter__(self):
        return self

for value in RandomChoiceIterator([1, 2, 3], num_iters=5):
    print(value)