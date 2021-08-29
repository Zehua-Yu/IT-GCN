# -*- coding: utf-8 -*-
# @Time    : 2020/8/10 6:42 下午
# @Author  : Zehua Yu
# @Email   : 19zhyu@stu.edu.cn
# @File    : collect_9d.py
# @Software : PyCharm

import pandas as pd
import numpy as np
import csv
import os

input_original_data = 'time_series_covid19_confirmed_US_210515.csv'
output_confirmed_collection_ntran = 'Covid19_cad9_confirmed_collection_210515_ntran.csv'
output_confirmed_collection = 'Covid19_cad9_confirmed_collection_210515.csv'

d3 = ['Amador', 'Sacramento', 'Butte', 'Colusa', 'Del Norte', 'El Dorado',
      'Glenn', 'Humboldt', 'Lake', 'Lassen', 'Modoc', 'Nevada', 'Plumas',
      'Shasta', 'Siskiyou', 'Sutter', 'Yuba', 'Sierra', 'Tehama', 'Trinity',
      'Yolo']
d4 = ['San Francisco', 'San Mateo', 'Alameda', 'Contra Costa', 'Marin',
      'Monterey', 'Napa', 'San Benito', 'San Mateo', 'Santa Barbara', 'Santa Clara',
      'Solano', 'Sonoma', 'Stanislaus', 'Ventura']
d5 = ['Santa Cruz']
d6 = ['Fresno', 'Madera', 'San Luis Obispo', 'Tulare']
d7 = ['Los Angeles', 'Mendocino']
d8 = ['Riverside', 'San Bernardino']
d10 = ['San Joaquin', 'Inyo', 'Mariposa', 'Merced', 'Mono', 'Placer', 'Tuolumne']
d11 = ['San Diego', 'Alpine', 'Imperial', 'Kern', 'Kings']
d12 = ['Orange']

df_in = pd.read_csv(input_original_data, header=None)
se = []
for i in range(480):
    sum = 0
    for j in range(3262):
        city = df_in.iloc[j, 5]
        for k in range(len(d3)):
            if city == d3[k]:
                sum = sum + int(df_in.iloc[j, 11 + i])
    se.append(sum)
with open(output_confirmed_collection_ntran, "a") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(se)
    csv_file.close()
se = []
print('d3 is done.')
for i in range(480):
    sum = 0
    for j in range(3262):
        city = df_in.iloc[j, 5]
        for k in range(len(d4)):
            if city == d4[k]:
                sum = sum + int(df_in.iloc[j, 11 + i])
    se.append(sum)
with open(output_confirmed_collection_ntran, "a") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(se)
    csv_file.close()
print('d4 is done.')
se = []
for i in range(480):
    sum = 0
    for j in range(3262):
        city = df_in.iloc[j, 5]
        for k in range(len(d5)):
            if city == d5[k]:
                sum = sum + int(df_in.iloc[j, 11 + i])
    se.append(sum)
with open(output_confirmed_collection_ntran, "a") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(se)
    csv_file.close()
print('d5 is done.')
se = []
for i in range(480):
    sum = 0
    for j in range(3262):
        city = df_in.iloc[j, 5]
        for k in range(len(d6)):
            if city == d6[k]:
                sum = sum + int(df_in.iloc[j, 11 + i])
    se.append(sum)
with open(output_confirmed_collection_ntran, "a") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(se)
    csv_file.close()
print('d6 is done.')
se = []
for i in range(480):
    sum = 0
    for j in range(3262):
        city = df_in.iloc[j, 5]
        for k in range(len(d7)):
            if city == d7[k]:
                sum = sum + int(df_in.iloc[j, 11 + i])
    se.append(sum)
with open(output_confirmed_collection_ntran, "a") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(se)
    csv_file.close()
print('d7 is done.')
se = []
for i in range(480):
    sum = 0
    for j in range(3262):
        city = df_in.iloc[j, 5]
        for k in range(len(d8)):
            if city == d8[k]:
                sum = sum + int(df_in.iloc[j, 11 + i])
    se.append(sum)
with open(output_confirmed_collection_ntran, "a") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(se)
    csv_file.close()
print('d8 is done.')
se = []
for i in range(480):
    sum = 0
    for j in range(3262):
        city = df_in.iloc[j, 5]
        for k in range(len(d10)):
            if city == d10[k]:
                sum = sum + int(df_in.iloc[j, 11 + i])
    se.append(sum)
with open(output_confirmed_collection_ntran, "a") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(se)
    csv_file.close()
print('d10 is done.')
se = []
for i in range(480):
    sum = 0
    for j in range(3262):
        city = df_in.iloc[j, 5]
        for k in range(len(d11)):
            if city == d11[k]:
                sum = sum + int(df_in.iloc[j, 11 + i])
    se.append(sum)
with open(output_confirmed_collection_ntran, "a") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(se)
    csv_file.close()
print('d11 is done.')
se = []
for i in range(480):
    sum = 0
    for j in range(3262):
        city = df_in.iloc[j, 5]
        for k in range(len(d12)):
            if city == d12[k]:
                sum = sum + int(df_in.iloc[j, 11 + i])
    se.append(sum)
with open(output_confirmed_collection_ntran, "a") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(se)
    csv_file.close()
print('d12 is done.')
df4 = pd.read_csv(output_confirmed_collection_ntran, header=None)
df4.values
data = df4.iloc[:, :].values
data = list(map(list, zip(*data)))
data = pd.DataFrame(data)
data.to_csv(output_confirmed_collection, header=0, index=0)
os.remove(output_confirmed_collection_ntran)