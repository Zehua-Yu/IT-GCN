# -*- coding: utf-8 -*-
# @Time    : 2020/8/9 7:25 下午
# @Author  : Zehua Yu
# @Email   : 19zhyu@stu.edu.cn
# @File    : Error_analysis.py
# @Software : PyCharm

import pandas as pd
import csv
import numpy as np
import os



def MAPE(v_, v):
    '''
    Mean absolute percentage error.
    :param v: np.ndarray or int, ground truth.
    :param v_: np.ndarray or int, prediction.
    :return: int, MAPE averages on all elements of input.
    '''
    # re = []
    # for i in range(8):
    #     dif_c = []
    #     for j in range(51):
    #         if j >= 0:
    #             dif = np.abs(v_.iloc[i, j] - v.iloc[i + 77 + 8, j]) / (v.iloc[i + 77 + 8, j] + 1e-5)
    #             dif_c.append(dif)
    #     re.append(np.mean(dif_c))
    # return re
    return np.mean(np.abs(v_ - v) / (v + 1e-5))


def sMAPE(v_, v):
    '''
    Mean absolute percentage error.
    :param v: np.ndarray or int, ground truth.
    :param v_: np.ndarray or int, prediction.
    :return: int, MAPE averages on all elements of input.
    '''
    re = []
    for i in range(8):
        dif_c = []
        sum2 = 0
        for j in range(51):
            if j >= 0:
                dif = np.abs(v_.iloc[i, j] - v.iloc[i + 77 + 8, j]) / (
                            (np.abs(v.iloc[i + 77 + 8, j]) + np.abs(v_.iloc[i, j])) / 2 + 1e-5)
                dif_c.append(dif)
                sum2 = dif + sum2
        re.append(np.mean(dif_c))
    return re


def RMSE(v_, v):
    '''
    Mean squared error.
    :param v: np.ndarray or int, ground truth.
    :param v_: np.ndarray or int, prediction.
    :return: int, RMSE averages on all elements of input.
    '''
    # re = []
    # for i in range(8):
    #     dif_c = []
    #     for j in range(51):
    #         if j >= 0:
    #             dif = (v_.iloc[i, j] - v.iloc[i + 77 + 8, j]) ** 2
    #             dif_c.append(dif)
    #     re.append(np.sqrt(np.mean(dif_c)))
    # return re
    return np.sqrt(np.mean((v_ - v) ** 2))


def MAE(v_, v):
    '''
    Mean absolute error.
    :param v: np.ndarray or int, ground truth.
    :param v_: np.ndarray or int, prediction.
    :return: int, MAE averages on all elements of input.
    '''

    # re = []
    # for i in range(8):
    #     dif_c = []
    #     for j in range(51):
    #         if j >= 0:
    #             dif = np.abs(v_.iloc[i, j] - v.iloc[i + 77 + 8, j])
    #             dif_c.append(dif)
    #     re.append(np.mean(dif_c))
    return np.mean(np.abs(v_ - v))


lr = 3
df_pre = pd.read_csv(f'pre_{lr}.csv', header=None)
df_2diff = pd.read_csv('2diff_re.csv', header=None)
df_1diff = pd.read_csv('1diff_re.csv', header=None)
out_2diff = f're_2diff{lr}.csv'
out_1diff = f'pre_confirm.csv'
err_pre = f'err_pre_{lr}.csv'
df_gt = pd.read_csv('ground_truth.csv', header=None)


# for i in range(17):
#     timese = []
#     for j in range(51):
#         sum1 = float(df_pre.iloc[i, j].strip('[]')) + int(df_2diff.iloc[i, j])
#         timese.append(sum1)
#     with open(out_2diff, "a") as csv_file:
#         writer = csv.writer(csv_file)
#         writer.writerow(timese)
#         csv_file.close()
# df_out_2diff = pd.read_csv(out_2diff, header=None)
# for i in range(17):
#     timese = []
#     for j in range(51):
#         sum1 = float(df_out_2diff.iloc[i, j]) + int(df_1diff.iloc[i, j])
#         if sum1 < 0:
#             sum1 = 0
#         timese.append(int(sum1))
#     with open(out_1diff, "a") as csv_file:
#         writer = csv.writer(csv_file)
#         writer.writerow(timese)
#         csv_file.close()

df_pre_confirm = pd.read_csv(out_1diff, header=None)
for j in range(17):
    err_arr = []
    y = 0
    y_ = 0
    for i in range(51):
        y = y + df_gt.iloc[j, i]
        y_ = y_ + df_pre_confirm.iloc[j, i]
        # y.append(df_gt.iloc[j, i])
        # y_.append(df_pre_confirm.iloc[j + 1, i])
    y = np.array(y)
    y_ = np.array(y_)
    err_arr.append(y)
    err_arr.append(y_)
    err_arr.append(MAE(y_, y))
    err_arr.append(RMSE(y_, y))
    err_arr.append(MAPE(y_, y))
    with open(err_pre, "a") as csv_file:
         writer = csv.writer(csv_file)
         writer.writerow(err_arr)
         csv_file.close()