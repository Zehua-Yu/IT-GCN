# -*- coding: utf-8 -*-
# @Time    : 2020/8/10 11:13 上午
# @Author  : Zehua Yu
# @Email   : 19zhyu@stu.edu.cn
# @File    : flow_draw.py
# @Software : PyCharm


import numpy as np
import matplotlib.pyplot as plt
import datetime
import matplotlib as mpl  # 设置x轴范围
import pandas as pd
from scipy import signal

df_ts = pd.read_csv('err_precad933.csv', header=None)
dft = pd.read_csv('tendency5.csv', header=None)
print(dft.iloc[0, :])
#df_gt = pd.read_csv('gt_flow31.csv', header=None)
#df1 = pd.read_csv('flow_V_9.csv', header=None)
dfd1 = pd.read_csv('Covid19_V_cad9_confirmed_collection_0809_1diff_51.csv', header=None)
dfsi = pd.read_csv('pre_confirmcad9.csv', header=None)
df_tend = pd.read_csv('tend5_pre.csv', header=None)
max_er = []
min_er = []
gt = []
mean = []
sumt = 0
sumtt = []
re = []
ooo=0
sum = []
sum1 = []
tendency = [180.845714285726, -1719.19999999999, 429.754285714293, 3574.70857142858,
            -1055.33714285714, 1054.91743697479, -639.827983193274, -2166.57340336134,
            -3219.31882352941, 1260.93575630253, 1959.19033613446, 2899.44491596639,
            342.699495798322, 393.954075630256, -2762.79134453781, -3476.53676470588,
            -3381.28218487395, 3563.97239495799, 5008.22697478992, -921.518445378146, -1326.26386554621]
single = []
singlegt = []
for i in range(21):
    single.append(dfsi.iloc[i, 8])
    singlegt.append(dfd1.iloc[i+120, 8])
for i in range(10):
    sum.append(df_ts.iloc[i, 1])
        #sum.append(df1.iloc[i, j])
    sum1.append(df_ts.iloc[i, 0])
    mean = sum
    gt = sum1
    # mean.append(np.mean(sum))
    # gt.append(np.mean(sum1))
print(mean)
print(gt)

re = mean
fig = plt.figure(figsize=(7, 5))
plt.rcParams['figure.dpi'] = 100000  # 分辨率
ax = fig.add_subplot(111)
start = datetime.datetime(2020, 5, 9)
stop = datetime.datetime(2020, 5, 19)
days = datetime.timedelta(10)  # 10天
delta = datetime.timedelta(1)  # 设定日期的间隔
dates = mpl.dates.drange(start, stop, delta)
ax = plt.gca()
outp = []
outp1 = []
td = [9777.94387624567, 11049.486107620356, 10081.254631434433, 10470.887526657269, 10396.791148730836, 10179.725853578355, 10401.018091963299, 10172.840548098122, 10255.775874456649, 10204.596109966356, 10155.102405794341, 10180.29596120869, 10118.339941864413, 10125.754602800775, 10099.275314121109, 10080.493162926898, 10074.004213165901, 10051.861883832376, 10045.294889840905, 10031.264174467975]
de = [4852.281309636861, 1499.5179034007351, 6220.915716306501, 5671.648685545755, 3117.052291375967, 2071.9062860052536, 1037.5786143592723, 4287.63273630405, 3187.7320125882998, 9062.53509429487, 2816.667465993256, 5388.089197999574, 200.10752757113005, 3914.2551878127324, 2674.8925806142925, 7675.319317795289, 5584.73269514727, 4917.9404869352875, 3266.7632726955853, 1018.7952612196495]

ax.plot(dates, sum, label='Prediction', marker="x", lw=1.5, color='blue')
ax.plot(dates, sum1, label='Ground Turth', marker="o", lw=1.5, color='red')
#ax.plot(dates, outp, label='1', marker="o", lw=1.5, color='green')
er = []




# ax.plot(dates, re, 'y-', color='grey')
# ax.plot(dates, re, 'o', color='red')
# ax.plot(dates, gt, 'y-', color='blue')
# ax.plot(dates, gt, 'o', color='brown')
date_format = mpl.dates.DateFormatter('%m-%d')
ax.xaxis.set_major_formatter(date_format)
#fig.autofmt_xdate()
#plt.grid(True)
font1 = {'family': 'Times New Roman', 'weight': 'normal', 'size': 15}
plt.legend(loc=0, prop=font1)
font2 = {'family': 'Times New Roman', 'weight': 'normal', 'size': 20}
plt.axis('tight')
plt.xlabel('Date', font2)
plt.ylabel('Infected Cases', font2)
plt.tick_params(labelsize=15)
#plt.title('PeMSD3(Sacramento) of California from 2020 3.4 to 4.18')

plt.show()
