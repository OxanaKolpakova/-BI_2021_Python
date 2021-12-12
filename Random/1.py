import random
import time
import matplotlib.pyplot as plt
import numpy as np


def Random_Plot(number=100):
    time_list = []
    for i in range(number):
        start_time = time.time()
        for j in range(number-i, number):
            random.random()
        time_list.append(time.time() - start_time)
    # print(time_list)
    plt.plot(range(number), time_list)
    plt.title("Random.Random")
    plt.xlabel("number")
    plt.ylabel("time")
    plt.show()


def NP_Random_Plot(number=100):
    time_list = []
    for i in range(number):
        start_time = time.time()
        np.random.uniform(0, 1, i)
        time_list.append(time.time() - start_time)
    # print(time_list)
    plt.plot(range(number), time_list)
    plt.title("Numpy.Random")
    plt.xlabel("number")
    plt.ylabel("time")
    plt.show()


NP_Random_Plot()
