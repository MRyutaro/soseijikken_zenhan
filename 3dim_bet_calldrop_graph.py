import pandas as pd
import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os

# groupのところだけ変える。
# 自分のカード、自分のベット、相手の決定、頻度の４変数。頻度は色で表す
group = 0
game_count = 0

txt_path = list()
csv_path = list()
my_card = list()
my_bet = list()
your_dicision = list()
int_my_card = list()
int_your_bet = list()


def main():
    dir_ex_check()
    get_group_and_gamecount()
    setup_path()
    txt_to_csv()
    csv_reader()
    mk_graph()


def dir_ex_check():
    if(os.path.isdir('C:/Users/m2002/Programs/Python/soseijikken/png') == False):
        os.mkdir('C:/Users/m2002/Programs/Python/soseijikken/png')
    if(os.path.isdir('C:/Users/m2002/Programs/Python/soseijikken/csv') == False):
        os.mkdir('C:/Users/m2002/Programs/Python/soseijikken/csv')


def get_group_and_gamecount():
    global group, game_count
    while(1):
        group = int(input('相手のグループ番号は？半角数字で入力してください。'))
        if(os.path.isfile(f'C:/Users/m2002/Programs/Python/soseijikken/txt/log{group}-1.txt') == False):
            print('ファイルがありません。もう一度入力してください。\n')
        # else:
        #     break

        game_count = int(input('ゲーム回数は何回？半角数字で入力してください。'))
        if(os.path.isfile(f'C:/Users/m2002/Programs/Python/soseijikken/txt/log{group}-{game_count}.txt') == False):
            print('そんなにゲームをしていません。もう一度入力してください。\n')
        else:
            break


def setup_path():
    global group, txt_path, csv_path, game_count
    for i in range(game_count):
        txt_path.append(
            f'C:/Users/m2002/Programs/Python/soseijikken/txt/log{group}-{i+1}.txt')
        csv_path.append(
            f'C:/Users/m2002/Programs/Python/soseijikken/csv/log{group}-{i+1}.csv')


def txt_to_csv():
    global txt_path, csv_path, game_count
    read_text_file = list()
    for i in range(game_count):
        if(os.path.isfile(csv_path[i]) == False):
            read_text_file.append(pd.read_csv(txt_path[i]))
            read_text_file[i].to_csv(csv_path[i], index=False)


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


def setup_marker(str):
    if(str == 0):
        m = 'o'
    elif(str == 1):
        m = '^'
    else:
        m = '*'
    return m


def csv_reader():

    global csv_path, my_card, my_bet, your_dicision, int_my_card, int_your_bet, game_count
    f = list()
    for i in range(game_count):
        f = open(csv_path[i], 'r')
        reader = csv.reader(f)
        for row in reader:
            # indexありでcsvファイルにするとrow[0]はindexになる。だから30行目で、indexなしで保存した。
            my_card.append(float(row[3]))
            my_bet.append(float(row[5]))
            your_dicision.append(row[6])
        # print(my_card)
        # print(my_bet)
        # print(your_dicision)
    your_dicision = digits_dicision(your_dicision)


def mk_graph():
    global my_card, my_bet, your_dicision, group, game_count

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.set_xlabel('my_card')
    ax.set_ylabel('my_bet')
    ax.set_zlabel('your_dicision(n=o,c=^,d=*)')

    for i in range(len(my_card)):
        x = my_card[i]
        y = my_bet[i]
        z = your_dicision[i]
        m = setup_marker(z)
        ax.scatter(x, y, z, marker=m, alpha=0.2, color='red')

    plt.title(f'group-{group}')
    plt.show()

    fig.savefig(
        f'C:/Users/m2002/Programs/Python/soseijikken/png/3dim_{group}.png')


if __name__ == '__main__':
    main()
