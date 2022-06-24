from re import I
import pandas as pd
import csv
import matplotlib.pyplot as plt
import os


group = [7, 8, 10, 11]
game_count = 3
txt_path = list()
csv_path = list()
my_card = list()
your_card = list()
my_dici = list()


def main():
    global my_card, your_card, my_dici
    # init
    dir_ex_check()
    # each group
    for group_num in range(len(group)):
        path_setup(group_num)
        txt_to_csv(group_num)
        csv_reader(group_num)

    check_miss()
    # print("----------------------my_card---------------------------\n")
    # print(my_card)
    # print("\n-----------------------------your_card-----------------------------------\n")
    # print(your_card)
    # print("\n-------------------------------my_dici---------------------------------------\n")
    # print(my_dici)


def dir_ex_check():
    if(os.path.isdir('png') == False):
        os.mkdir('png')
    if(os.path.isdir('csv') == False):
        os.mkdir('csv')


def path_setup(group_num):
    global group, txt_path, csv_path, game_count
    tmp_txt_path = []
    tmp_csv_path = []
    for i in range(game_count):
        tmp_txt_path.append(
            f'txt/log{group[group_num]}-{i+1}.txt')
        tmp_csv_path.append(
            f'csv/log{group[group_num]}-{i+1}.csv')
    txt_path.append(tmp_txt_path)
    csv_path.append(tmp_csv_path)


def txt_to_csv(group_num):
    global txt_path, csv_path, game_count
    read_text_file = list()
    for i in range(game_count):
        if(os.path.isfile(csv_path[group_num][i]) == False):
            read_text_file.append(pd.read_csv(txt_path[i]))
            read_text_file[i].to_csv(csv_path[group_num][i], index=False)


def csv_reader(group_num):
    global csv_path, my_card, your_card, game_count, my_dici
    f = list()
    tmp_game_count = 0
    tmp_your_card = []
    tmp_my_card = []
    tmp_my_dici = []

    for i in range(game_count):
        f = open(csv_path[group_num][i], 'r')
        reader = csv.reader(f)
        for row in reader:
            # indexありでcsvファイルにするとrow[0]はindexになる。だから30行目で、indexなしで保存した。
            tmp_game_count += 1
            tmp_your_card.append(float(row[2]))
            tmp_my_card.append(float(row[3]))
            tmp_my_dici.append(str(row[7]))

    your_card.append(tmp_your_card)
    my_card.append(tmp_my_card)
    my_dici.append(tmp_my_dici)


def check_miss():
    global your_card, my_card, my_dici, group

    for i in range(len(your_card)):
        tmp_in_game_count = 0
        tmp_c_count = 0
        tmp_d_count = 0
        tmp_c_miss_count = 0
        tmp_d_miss_count = 0

        for j in range(len(your_card[i])):
            tmp_in_game_count += 1
            if my_dici[i][j] == "c":
                tmp_c_count += 1
                if my_card[i][j] < your_card[i][j]:
                    tmp_c_miss_count += 1
            elif my_dici[i][j] == "d":
                tmp_d_count += 1
                if my_card[i][j] >= your_card[i][j]:
                    tmp_d_miss_count += 1

        tmp_c_miss_ratio = tmp_c_miss_count/tmp_c_count
        tmp_d_miss_ratio = tmp_d_miss_count/tmp_d_count

        print(
            f'\n-----------------------{group[i]}班-----------------------------')
        print(f'試合回数 = {tmp_in_game_count}')
        print(f'コールした回数 = {tmp_c_count}')
        print(f'ドロップした回数 = {tmp_d_count}')
        print(f'コールしたときミスした回数 = {tmp_c_miss_count}')
        print(f'ドロップしたときミスした回数 = {tmp_d_miss_count}')
        print(f'コールしたときミスした割合 = {round(tmp_c_miss_ratio*100, 1)}%')
        print(f'ドロップしたときミスした割合 = {round(tmp_d_miss_ratio*100, 1)}%')
        print(
            f'判断ミスした割合 = {round((tmp_d_miss_ratio+tmp_c_miss_ratio)*100, 1)}%')


if __name__ == '__main__':
    main()
