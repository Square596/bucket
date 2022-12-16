import numpy as np
from multiprocessing import Pool
from matplotlib import pyplot as plt
import time
import os


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


low = 10**3
high = 10**4
size = 10**6
repeats = 3 # закон больших чисел никто не отменял, хоть 3 и не особо большое)
numbers = np.random.randint(low=low, high=high, size=(size,repeats))

if __name__ == '__main__':
    results = {}
    count_cpu = os.cpu_count()
    for num_cpu in range(1, count_cpu + 1):
        results[num_cpu] = []
    for repeat in range(repeats):
        for num_cpu in range(1, count_cpu + 1):
            pool = Pool(num_cpu)
            start_time = time.time()
            pool.map(factorize, numbers[:,repeat])
            work_time = time.time() - start_time
            results[num_cpu].append(work_time)
    
    for num_cpu in range(1, count_cpu + 1):
        results[num_cpu] = np.mean(results[num_cpu]) # Усредненеие по этим 3 повторам

    plt.figure(figsize=(20,10))
    plt.plot(results.keys(), results.values())
    plt.xlabel('Количество используемых ядер')
    plt.ylabel('Время вычисления, с')
    plt.savefig('results.png')
    print('Выполнение завершено!')
