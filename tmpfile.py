import pandas as pd
import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os

group = 11
game_count = 3

my_card = [11.0, 5.0, 3.0, 6.0, 4.0, 4.0, 12.0, 10.0, 4.0, 5.0, 3.0, 12.0, 13.0, 7.0, 4.0, 8.0, 12.0, 12.0, 12.0, 11.0, 10.0, 4.0, 8.0, 13.0, 14.0, 11.0, 5.0, 10.0, 11.0, 4.0, 5.0, 7.0, 10.0, 12.0, 12.0, 8.0, 2.0, 12.0, 7.0, 5.0, 14.0, 9.0, 5.0, 7.0, 2.0, 12.0, 6.0, 6.0, 4.0, 11.0, 11.0, 13.0, 11.0, 7.0, 10.0, 8.0, 13.0, 12.0, 9.0, 11.0, 10.0, 3.0, 12.0, 12.0, 11.0, 13.0, 6.0, 5.0, 3.0, 5.0, 5.0, 2.0, 7.0, 14.0, 14.0, 4.0, 4.0, 14.0, 7.0, 6.0, 2.0, 11.0, 7.0, 6.0, 9.0, 8.0, 11.0, 4.0, 3.0, 6.0, 11.0, 3.0, 8.0, 2.0, 9.0, 6.0, 4.0, 10.0, 11.0,
           12.0, 2.0, 2.0, 3.0, 11.0, 13.0, 4.0, 8.0, 11.0, 3.0, 6.0, 11.0, 2.0, 5.0, 13.0, 8.0, 4.0, 13.0, 2.0, 2.0, 9.0, 7.0, 6.0, 2.0, 14.0, 5.0, 4.0, 3.0, 10.0, 13.0, 12.0, 10.0, 3.0, 7.0, 5.0, 12.0, 12.0, 5.0, 3.0, 14.0, 9.0, 10.0, 6.0, 2.0, 10.0, 6.0, 9.0, 10.0, 9.0, 9.0, 2.0, 8.0, 2.0, 9.0, 11.0, 8.0, 2.0, 14.0, 11.0, 14.0, 5.0, 14.0, 11.0, 3.0, 3.0, 11.0, 12.0, 4.0, 4.0, 12.0, 13.0, 2.0, 4.0, 3.0, 11.0, 2.0, 12.0, 12.0, 7.0, 8.0, 3.0, 9.0, 2.0, 9.0, 9.0, 12.0, 6.0, 7.0, 6.0, 11.0, 9.0, 6.0, 13.0, 10.0, 11.0, 5.0, 10.0, 13.0, 12.0, 13.0, 5.0]
my_bet = [1.1, 1.0, 1.0, 2.0, 1.0, 2.0, 1.0, 1.0, 2.0, 1.0, 2.0, 2.0, 1.0, 1.0, 2.0, 2.0, 1.0, 1.0, 2.0, 1.0, 3.0, 1.0, 1.0, 3.0, 1.0, 3.0, 2.0, 1.0, 3.0, 2.0, 1.0, 3.0, 5.0, 5.0, 2.0, 1.0, 1.0, 5.0, 4.0, 3.0, 5.0, 1.0, 2.0, 3.0, 3.0, 1.0, 2.0, 1.0, 2.0, 2.0, 2.0, 3.0, 5.0, 1.0, 5.0, 5.0, 1.0, 4.0, 4.0, 1.0, 1.0, 2.0, 4.0, 2.0, 1.0, 2.0, 5.0, 2.0, 1.0, 3.0, 1.0, 3.0, 3.0, 1.0, 5.0, 2.0, 2.0, 1.0, 2.0, 1.0, 5.0, 2.0, 1.0, 1.0, 2.0, 1.0, 1.0, 2.0, 5.0, 1.0, 5.0, 5.0, 3.0, 1.0, 1.0, 5.0, 1.0, 1.0, 5.0,
          1.0, 1.0, 1.0, 1.0, 3.0, 1.0, 4.0, 3.0, 1.0, 1.0, 1.0, 1.0, 2.0, 3.0, 3.0, 3.0, 4.0, 4.0, 1.0, 5.0, 2.0, 3.0, 1.0, 5.0, 1.0, 5.0, 2.0, 4.0, 4.0, 1.0, 2.0, 5.0, 1.0, 2.0, 3.0, 2.0, 4.0, 1.0, 3.0, 1.0, 2.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 2.0, 1.0, 2.0, 2.0, 1.0, 1.0, 1.0, 1.0, 2.0, 2.0, 2.0, 2.0, 1.0, 1.0, 2.0, 1.0, 1.0, 2.0, 5.0, 3.0, 4.0, 3.0, 5.0, 2.0, 4.0, 1.1, 2.0, 2.0, 2.0, 2.0, 1.0, 1.0, 2.0, 1.0, 2.0, 2.0, 1.0, 1.0, 2.0, 1.0, 2.0, 2.0, 1.0, 2.0, 2.0, 2.0, 2.0, 1.0, 2.0, 1.0, 1.0, 1.0]
your_dicision = ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'd', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'c', 'n', 'n', 'd', 'n', 'n', 'n', 'n', 'd', 'n', 'n', 'n', 'd', 'd', 'd', 'n', 'n', 'd', 'd', 'n', 'd', 'n', 'n', 'd', 'n', 'n', 'd', 'n', 'n', 'n', 'd', 'n', 'd', 'n', 'd', 'd', 'n', 'd', 'd', 'n', 'n', 'n', 'd', 'd', 'n', 'd', 'd', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'd', 'n', 'n', 'n', 'n', 'n', 'd', 'd', 'n', 'n', 'd', 'n', 'n', 'n', 'n', 'n', 'd', 'n', 'd', 'n', 'n', 'd', 'n', 'n',
                 'n', 'n', 'n', 'n', 'n', 'd', 'n', 'd', 'd', 'n', 'n', 'n', 'n', 'n', 'n', 'd', 'c', 'n', 'd', 'n', 'n', 'd', 'c', 'n', 'n', 'n', 'd', 'n', 'n', 'd', 'n', 'd', 'd', 'n', 'n', 'n', 'n', 'd', 'n', 'n', 'n', 'c', 'd', 'n', 'n', 'n', 'n', 'n', 'd', 'n', 'd', 'n', 'd', 'n', 'n', 'n', 'n', 'n', 'n', 'd', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'd', 'n', 'd', 'd', 'n', 'n', 'n', 'n', 'n', 'd', 'n', 'n', 'n', 'n', 'd', 'n', 'd', 'c', 'n', 'n', 'n', 'n', 'd', 'c', 'n', 'd', 'd', 'd', 'n', 'n', 'd', 'n', 'n', 'n']


def digits_dicision(array):
    for i in range(len(array)):
        if(array[i] == 'c'):
            array[i] = 1
        elif(array[i] == 'd'):
            array[i] = 2
        elif(array[i] == 'n'):
            array[i] = 0
        else:
            print('エラー')
    return array


your_dicision = digits_dicision(your_dicision)


def setup_marker(str):
    if(str == 0):
        m = 'o'
    elif(str == 1):
        m = '^'
    else:
        m = '*'
    return m


def mk_graph():
    global my_card, my_bet, your_dicision, group, game_count

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.set_xlabel('my_card')
    ax.set_ylabel('my_bet')
    ax.set_zlabel('your_dicision(n=0,c=1,d=2)')

    for i in range(len(my_card)):
        x = my_card[i]
        y = my_bet[i]
        z = your_dicision[i]
        m = setup_marker(z)
        ax.scatter(x, y, z, marker=m, alpha=0.2, color='red')

    plt.title(f'group-{group}')
    plt.show()


mk_graph()
