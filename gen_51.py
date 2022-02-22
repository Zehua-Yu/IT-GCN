
import pandas as pd
import numpy as np
import csv
import os

"""
提取下载原始数据集中的各州的确诊总数时间序列，并进行差分处理，输出的即是可直接使用的预测数据集

参数设置(parameters settings)
diff：差分次数
days：所收集天数
"""

diff = 1
days = 149
input_original_data = 'time_series_covid19_confirmed_US_210515.csv'
output_confirmed_collection_ntran = 'Covid19_US_confirmed_collection_210515_ntran.csv'
output_confirmed_collection = 'Covid19_US_confirmed_collection_210515.csv'
states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California',
          'Colorado', 'Connecticut', 'Delaware', 'District of Columbia',
          'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana',
          'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland',
          'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi',
          'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire',
          'New Jersey', 'New Mexico', 'New York', 'North Carolina',
          'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania',
          'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee',
          'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia',
          'Wisconsin', 'Wyoming']
df1 = pd.read_csv(input_original_data, header=None)
for i in range(51):
    state = states[i]
    A = []
    for j in range(days):
        sum = 0
        for k in range(3262):
            if state == df1.iloc[k, 6]:
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