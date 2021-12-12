import random
import time
import matplotlib.pyplot as plt
import numpy as np


def sort_check(list):
    for i in range(len(list)-1):
        if list[i] > list[i+1]:
            return False
    return True


def monkey_sort(num_list):
    while sort_check(num_list) is False:
        random.shuffle(num_list)
    return(num_list)


def main(number=10, iter=5):    # max number of list and iterations
    time_list = []
    mean_time = []
    var_time = []
    for i in range(number):     # range of array
        for j in range(iter):        # times
            start_time = time.time()
            list = np.random.randint(0, 100, i)
            monkey_sort(list)
            time_list.append(time.time() - start_time)
        mean_time.append(np.mean(time_list))
        var_time.append(np.var(time_list))
    plt.plot(range(number), mean_time, label="mean")
    plt.plot(range(number), var_time, label="variance")
    plt.legend(loc='upper left', frameon=False)
    plt.title("Mean, Variance")
    plt.xlabel("number")
    plt.ylabel("mean, variance")
    plt.show()


main()
