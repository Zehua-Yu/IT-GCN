# -*- coding: utf-8 -*-
# @Time    : 2020/8/8 11:15 下午
# @Author  : Zehua Yu
# @Email   : 19zhyu@stu.edu.cn
# @File    : collect_for_ca.py
# @Software : PyCharm


import pandas as pd
import numpy as np
import csv
import os

"""
提取下载原始数据集中的各城市的确诊总数时间序列，并进行差分处理，输出的即是可直接使用的预测数据集

参数设置
diff：差分次数
days：所收集天数
"""


diff = 1
days = 480
input_original_data = 'time_series_covid19_confirmed_US_210515.csv'
output_confirmed_collection_ntran = 'Covid19_confirmed_collection_210515_ntran.csv'
output_confirmed_collection = 'Covid19_confirmed_collection_210515.csv'
states = ['Alameda', 'Alpine', 'Amador', 'Butte', 'Calaveras',
          'Colusa', 'Contra Costa', 'Del Norte', 'El Dorado',
          'Fresno', 'Glenn', 'Humboldt', 'Imperial', 'Inyo', 'Kern',
          'Kings', 'Lake', 'Lassen', 'Los Angeles', 'Madera', 'Marin',
          'Mariposa', 'Mendocino', 'Merced', 'Modoc',
          'Mono', 'Monterey', 'Napa', 'Nevada', 'Orange',
          'Placer', 'Plumas', 'Riverside', 'Sacramento',
          'San Benito', 'San Bernardino', 'San Diego', 'San Francisco', 'San Joaquin',
          'San Luis Obispo', 'San Mateo', 'Santa Barbara', 'Santa Clara',
          'Santa Cruz', 'Shasta', 'Sierra', 'Siskiyou', 'Solano', 'Sonoma',
          'Stanislaus', 'Sutter', 'Tehama', 'Trinity', 'Tulare', 'Tuolumne', 'Ventura',
          'Yolo', 'Yuba']
df1 = pd.read_csv(input_original_data, header=None)
for i in range(58):
    state = states[i]
    A = []
    for j in range(days):
        sum = 0
        for k in range(3262):
            if state == df1.iloc[k, 5]:
                sum = sum + int(df1.iloc[k, j + 11])
        if sum > 0:
            A.append(sum)
        else:
            A.append(sum)
    with open(output_confirmed_collection_ntran, "a") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(A)
        csv_file.close()
    print(state, 'is done')
df2 = pd.read_csv(output_confirmed_collection_ntran, header=None)
df2.values
data = df2.iloc[:, :].values
data = list(map(list, zip(*data)))
data = pd.DataFrame(data)
data.to_csv(output_confirmed_collection, header=0, index=0)
#
# d3 = ['Amador', 'Sacramento', 'Butte', 'Colusa', 'Del Norte', 'El Dorado',
#       'Glenn', 'Humboldt', 'Lake', 'Lassen', 'Modoc', 'Nevada', 'Plumas',
#       'Shasta', 'Siskiyou', 'Sutter', 'Yuba', 'Sierra', 'Tehama', 'Trinity',
#       'Yolo']
# d4 = ['San Francisco', 'San Mateo', 'Alameda', 'Contra Costa', 'Marin',
#       'Monterey', 'Napa', 'San Benito', 'San Mateo', 'Santa Barbara', 'Santa Clara',
#       'Solano', 'Sonoma', 'Stanislaus', 'Ventura']
# d5 = ['Santa Cruz']
# d6 = ['Fresno', 'Madera', 'San Luis Obispo', 'Tulare']
# d7 = ['Los Angeles', 'Mendocino']
# d8 = ['Riverside', 'San Bernardino']
# d10 = ['San Joaquin', 'Inyo', 'Mariposa', 'Merced', 'Mono', 'Placer', 'Tuolumne']
# d11 = ['San Diego', 'Alpine', 'Imperial', 'Kern', 'Kings']
# d12 = ['Orange']
#
# df3 = pd.read_csv('Covid19_cad9_confirmed_collection_210515.csv', header=None)
# New_add_diff_ntran = f'Covid19_cad9_confirmed_collection_210515_{diff}diff_ntran.csv'
# New_add_diff = f'Covid19_V_cad9_confirmed_collection_210515_{diff}diff_51.csv'
# sum_c = 0
# timeseries = []
# for a in range(9):
#     timeseries = []
#     sum_c = 0
#     for i in range(days):
#         if i >= 0:
#             sum_c = df3.iloc[i, a]
#             timeseries.append(sum_c)
#     timeseries = np.diff(timeseries, n=diff)
#     with open(New_add_diff_ntran, "a") as csv_file:
#         writer = csv.writer(csv_file)
#         writer.writerow(timeseries)
#         csv_file.close()
# df4 = pd.read_csv(New_add_diff_ntran, header=None)
# df4.values
# data = df4.iloc[:, :].values
# data = list(map(list, zip(*data)))
# data = pd.DataFrame(data)
# data.to_csv(New_add_diff, header=0, index=0)
# os.remove(New_add_diff_ntran)
# #os.remove(output_confirmed_collection_ntran)
# os.remove(output_confirmed_collection)