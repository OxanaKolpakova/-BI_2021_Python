from itertools import zip_longest
import random
import matplotlib.pyplot as plt


def random_walk(num_steps=5000):
    coordinate_list = []
    x = []
    y = []
    coordinate = [0,0]
    step_list = [[0,1],[0,-1],[1,0],[-1,0]]
    for num in range(num_steps):
        step = random.choice(step_list)
        coordinate = [sum(i) for i in zip_longest(coordinate, step, fillvalue=0)]
        coordinate_list.append(coordinate)
    #print(coordinate_list)
    for j in range(len(coordinate_list)):
        x.append(coordinate_list[j][0])
        y.append(coordinate_list[j][1])
    fig, ax = plt.subplots()
    ax.scatter(x = x, y = y)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
  
    
random_walk()
