# -*- coding: utf-8 -*-
# @Time    : 2020/7/4 8:37 下午
# @Author  : Zehua Yu
# @Email   : 19zhyu@stu.edu.cn
# @File    : generate_arma_pa_and_eucl.py
# @Software : PyCharm

import pandas as pd
from statsmodels.tsa.arima_model import ARMA, ARIMA
import csv
import os
from scipy.spatial.distance import pdist
from scipy.spatial.distance import squareform

"""
利用V，对每个州（节点）进行ARMA参数求解，最后输出的即是欧式距离矩阵W
"""

diff = 1
df1 = pd.read_csv(f'Covid19_V_cad9_confirmed_collection_0809_{diff}diff_51.csv', header=None)
output_pa = f'Covid19_vector_pa_csd9_0809_{diff}diff.csv'
sum_c = 0
for i in range(9):
    timeseries = []
    if i >= 0:
        for j in range(146):
            timeseries.append(df1.iloc[j, i]+1)
        p = 5
        q = 0
        print(p, q)
 #       model = ARIMA(timeseries, order=(p, 1, q)).fit()
        model = ARMA(timeseries, order=(p, q)).fit()
        data_h = model.summary()
        print(data_h)
        B = []
        for k in range(p+q):
            B.append(data_h[k])
        with open(output_pa, "a") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(B)
            csv_file.close()
        print(i + 1, 'is done.')

output_eucl_ntran = f'Covid19_W_csd90809_{diff}diff_ntran.csv'
output_eucl = f'Covid19_W_csd90809_{diff}diff_51.csv'
df4 = pd.read_csv(output_pa, header=None)

#转置用
df4.values
data = df4.iloc[:, :].values
data = list(map(list, zip(*data)))
data = pd.DataFrame(data)
data.to_csv(output_eucl_ntran, header=0, index=0)
df2 = pd.read_csv(output_eucl_ntran, header=None)
vec = []
A = []
i = 0
j = 0
for i in range(9):
    for j in range(5):
        A.append(complex(df2.iloc[j, i])*10)
    vec.append(1)
    vec[i] = A
    A = []
# # A是一个向量矩阵：euclidean代表欧式距离
distA = pdist(vec, metric='euclidean')
# # 将distA数组变成一个矩阵
distB = squareform(distA)
for a in range(9):
    A = []
    for b in range(9):
        A.append(distB[a, b])
    with open(output_eucl, "a") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(A)
        csv_file.close()
os.remove(output_eucl_ntran)
os.remove(output_pa)
