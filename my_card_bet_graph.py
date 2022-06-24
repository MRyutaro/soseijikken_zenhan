import pandas as pd
import csv
import matplotlib.pyplot as plt
import os

# groupのところだけ変える。
group = 0
game_count = 0

txt_path = list()
csv_path = list()
your_card = list()
my_bet = list()
int_your_card = list()
int_my_bet = list()


def main():
    dir_ex_check()
    get_group_and_gamecount()
    path_setup()
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

        game_count = int(input('ゲーム回数は何回？半角数字で入力してください。'))
        if(os.path.isfile(f'C:/Users/m2002/Programs/Python/soseijikken/txt/log{group}-{game_count}.txt') == False):
            print('そんなにゲームをしていません。もう一度入力してください。\n')
        else:
            break


def path_setup():
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


def csv_reader():
    global csv_path, your_card, my_bet, int_your_card, int_my_bet, game_count
    f = list()
    for i in range(game_count):
        f = open(csv_path[i], 'r')
        reader = csv.reader(f)
        for row in reader:
            # indexありでcsvファイルにするとrow[0]はindexになる。だから30行目で、indexなしで保存した。
            your_card.append(float(row[2]))
            my_bet.append(float(row[5]))


def mk_graph():
    global your_card, my_bet, group, game_count
    x = your_card
    y = my_bet
    fig = plt.figure()
    plt.scatter(x, y, s=100, alpha=0.2)
    plt.title(f'group-{group}')
    plt.xlabel('your_card')
    plt.ylabel('my_bet')
    plt.show()

    fig.savefig(f'C:/Users/m2002/Programs/Python/soseijikken/png/my{group}.png')


if __name__ == '__main__':
    main()
