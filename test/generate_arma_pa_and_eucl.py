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
Input: V matrix [n(nodes), m(steps)]
Output: W matrix [n, n]
"""

'''
Parameters Setting
diff: In order to keep the time series of each node stable, it is necessary to carry out differential processing.
Here is the order setting of the difference (The difference is not performed here. It is completed when V is generated.
The setting here is to facilitate file reading and writing).
According to my experience, diff will not be greater than 3.
days: Number of days required.
df1: Input data.
output_pa: Output data.

p, q: The order of ARMA model. Sometimes the setting of parameters here will lead to an error. 
The reason is that when the time series of nodes in the cycle does not meet the input requirements of ARMA model, 
the solution is to change the parameter combination or find a new way to preprocess the data.
'''
diff = 3
days = 143
df1 = pd.read_csv(f'Covid19_V_US_confirmed_collection_0809_{diff}diff_51.csv', header=None)
output_pa = f'Covid19_vector_pa_ucc_0809_{diff}diff.csv'

sum_c = 0
for i in range(51):
    print(df1.iloc[0, i])
    print(i)
    timeseries = []
    if i >= 0:
        for j in range(days):
            timeseries.append(df1.iloc[j, i]+1)
        p = 4
        q = 0
        print(p, q)
        model = ARMA(timeseries, order=(p, q)).fit()
        data_h = model.summary()
        print(data_h) #print the ARMA parameters
        B = []
        for k in range(p+q):
            B.append(data_h[k])
        with open(output_pa, "a") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(B)
            csv_file.close()
        print('States', i + 1, 'is done.')

output_eucl_ntran = f'Covid19_W_ucc0809_{diff}diff_ntran.csv'
output_eucl = f'Covid19_W_0809_{diff}diff_51.csv'
df4 = pd.read_csv(output_pa, header=None)


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
for i in range(51):
    for j in range(p+q):
        A.append(complex(df2.iloc[j, i])*10)
    vec.append(1)
    vec[i] = A
    A = []

distA = pdist(vec, metric='euclidean')
distB = squareform(distA)
for a in range(51):
    A = []
    for b in range(51):
        A.append(distB[a, b])
    with open(output_eucl, "a") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(A)
        csv_file.close()
os.remove(output_eucl_ntran)
os.remove(output_pa)
