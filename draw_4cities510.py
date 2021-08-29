# -*- coding: utf-8 -*-
# @Time    : 2020/8/23 7:00 下午
# @Author  : Zehua Yu
# @Email   : 19zhyu@stu.edu.cn
# @File    : draw_4cities510.py
# @Software : PyCharm


import numpy as np
import matplotlib.pyplot as plt
import datetime
import matplotlib as mpl  # 设置x轴范围
import pandas as pd
from matplotlib.ticker import FuncFormatter

def Q_statistic(N, y1, y2, y3, y4):
    y = []
    for i in range(len(y1)):
        y.append(y1[i]+y2[i])
    sigma = np.var(y)
    SST = N * sigma
    SSW = np.var(y1) + sigma
    q = 1 - SSW/SST
    return q

def moving_average(x, n, type='simple'):
    x = np.asarray(x)
    if type == 'simple':
        weights = np.ones(n)
    else:
        weights = np.exp(np.linspace(-1., 0., n))

    weights /= weights.sum()

    a = np.convolve(x, weights, mode='full')[:len(x)]
    a[:n] = a[n]
    return a

df_ts = pd.read_csv('err_precad93long.csv', header=None)
dftraffic = pd.read_csv('flow_V_9.csv', header=None)
dftrpre = pd.read_csv('pre_flow73.csv', header=None)
df1 = pd.read_csv('Covid19_V_cad9_confirmed_collection_0809_1diff_51.csv', header=None)
dfpre = pd.read_csv('pre_confirmcad933.csv', header=None)
dfgt = pd.read_csv('gt_flow73.csv', header=None)


tfla_pre = []
tfla_gt = []
cola_pre = []
cola_gt = []

tfsa_pre = []
tfsa_gt = []
cosa_pre = []

tfba_pre = []
coba_pre = []

tfsd_pre = []
cosd_pre = []
for i in range(35):
    tfsa_pre.append(dftraffic.iloc[i+52, 0])
    tfba_pre.append(dftraffic.iloc[i+52, 1])
    tfla_pre.append(dftraffic.iloc[i+52, 4])
    tfsd_pre.append(dftraffic.iloc[i+52, 7])

    # tfsa_pre.append(float(dftrpre.iloc[i+2, 0].strip('[]')))
    # tfla_pre.append(float(dftrpre.iloc[i+2, 4].strip('[]')))

    cosa_pre.append(dfpre.iloc[i+56-7-14, 0])
    coba_pre.append(dfpre.iloc[i+56-7-14, 1])
    cola_pre.append(dfpre.iloc[i+56-7-14, 4])
    cosd_pre.append(dfpre.iloc[i+56-7-14, 7])

tfsa_acc = []
cosa_acc = []
tfla_acc = []
cola_acc = []

fig = plt.figure(figsize=(20, 25))
plt.rcParams['figure.dpi'] = 100000  # 分辨率

plt.subplot(421)
ax = plt.gca()
ma7 = moving_average(tfsa_pre, 7, 'simple')
ax.plot(tfsa_pre[6:36], label='Traffic Flow in North of CA', marker="^", markersize=15, lw=4, color='mediumseagreen')
ax.plot(ma7[6:36], label='7-days moving average', marker="o", markersize=15, lw=4, color='deeppink')
font1 = {'family': 'Times New Roman', 'weight': 'normal', 'size': 20}
ax.legend(loc=4, prop=font1)
font2 = {'family': 'Times New Roman', 'weight': 'normal', 'size': 25}
plt.axis('tight')
aasd = ['06-21', '06-28', '07-05', '07-12', '07-19']
plt.xticks(range(0, 35, 7), aasd, rotation=0)
plt.xlabel('Date', font2)
plt.ylabel('Total Flow', font2)
plt.tick_params(labelsize=20)
plt.tight_layout()
def formatnum(x, pos):
    return '$%.1f$x$10^{4}$' % (x/10000)
formatter = FuncFormatter(formatnum)
ax.yaxis.set_major_formatter(formatter)
plt.title('(a)', font2)

plt.subplot(423)
ax = plt.gca()
ma7 = moving_average(tfla_pre, 7, 'simple')
ax.plot(tfla_pre[6:36], label='Traffic Flow in LA/Ventura', marker="^", markersize=15, lw=4, color='mediumseagreen')
ax.plot(ma7[6:36], label='7-days moving average', marker="o", markersize=15, lw=4, color='deeppink')
font1 = {'family': 'Times New Roman', 'weight': 'normal', 'size': 20}
ax.legend(loc=4, prop=font1)
font2 = {'family': 'Times New Roman', 'weight': 'normal', 'size': 25}
plt.axis('tight')
aasd = ['06-21', '06-28', '07-05', '07-12', '07-19']
plt.xticks(range(0, 35, 7), aasd, rotation=0)
plt.xlabel('Date', font2)
plt.ylabel('Total Flow', font2)
plt.tick_params(labelsize=20)
plt.tight_layout()
def formatnum(x, pos):
    return '$%.1f$x$10^{4}$' % (x/10000)
formatter = FuncFormatter(formatnum)
ax.yaxis.set_major_formatter(formatter)
plt.title('(c)', font2)

plt.subplot(425)
ax = plt.gca()
ma7 = moving_average(tfba_pre, 7, 'simple')
ax.plot(tfba_pre[6:36], label='Traffic Flow in Bay Area', marker="^", markersize=15, lw=4, color='mediumseagreen')
ax.plot(ma7[6:36], label='7-days moving average', marker="o", markersize=15, lw=4, color='deeppink')
font1 = {'family': 'Times New Roman', 'weight': 'normal', 'size': 20}
ax.legend(loc=4, prop=font1)
font2 = {'family': 'Times New Roman', 'weight': 'normal', 'size': 25}
plt.axis('tight')
aasd = ['06-21', '06-28', '07-05', '07-12', '07-19']
plt.xticks(range(0, 35, 7), aasd, rotation=0)
plt.xlabel('Date', font2)
plt.ylabel('Total Flow', font2)
plt.tick_params(labelsize=20)
plt.tight_layout()
def formatnum(x, pos):
    return '$%.1f$x$10^{4}$' % (x/10000)
formatter = FuncFormatter(formatnum)
ax.yaxis.set_major_formatter(formatter)
plt.title('(e)', font2)

plt.subplot(427)
ax = plt.gca()
ma7 = moving_average(tfsd_pre, 7, 'simple')
ax.plot(tfsd_pre[6:36], label='Traffic Flow in San Diego/Imperial', marker="^", markersize=15, lw=4, color='mediumseagreen')
ax.plot(ma7[6:36], label='7-days moving average', marker="o", markersize=15, lw=4, color='deeppink')
font1 = {'family': 'Times New Roman', 'weight': 'normal', 'size': 20}
ax.legend(loc=4, prop=font1)
font2 = {'family': 'Times New Roman', 'weight': 'normal', 'size': 25}
plt.axis('tight')
aasd = ['06-21', '06-28', '07-05', '07-12', '07-19']
plt.xticks(range(0, 35, 7), aasd, rotation=0)
plt.xlabel('Date', font2)
plt.ylabel('Total Flow', font2)
plt.tick_params(labelsize=20)
plt.tight_layout()
def formatnum(x, pos):
    return '$%.1f$x$10^{4}$' % (x/10000)
formatter = FuncFormatter(formatnum)
ax.yaxis.set_major_formatter(formatter)
plt.title('(g)', font2)

ax = fig.add_subplot(422)
ax = plt.gca()
ma7 = moving_average(cosa_pre, 7, 'simple')
ax.plot(cosa_pre[6:36], label='Prediction in North of CA', marker="^", markersize=15, lw=4, color='deepskyblue')
ax.plot(ma7[6:36], label='7-days moving average', marker="s", markersize=15, lw=4, color='salmon')
aasd = ['06-21', '06-28', '07-05', '07-12', '07-19']
plt.xticks(range(0, 35, 7), aasd, rotation=0)
font1 = {'family': 'Times New Roman', 'weight': 'normal', 'size': 20}
ax.legend(loc=0, prop=font1)
font2 = {'family': 'Times New Roman', 'weight': 'normal', 'size': 25}
plt.axis('tight')
plt.xlabel('Date', font2)
plt.ylabel('Daily Infected Cases', font2)
plt.tick_params(labelsize=20)
plt.tight_layout()
plt.title('(b)', font2)

ax = fig.add_subplot(424)
ax = plt.gca()
ma7 = moving_average(cola_pre, 7, 'simple')
ax.plot(cola_pre[6:36], label='Prediction in LA/Ventura', marker="^", markersize=15, lw=4, color='deepskyblue')
ax.plot(ma7[6:36], label='7-days moving average', marker="s", markersize=15, lw=4, color='salmon')
aasd = ['06-21', '06-28', '07-05', '07-12', '07-19']
plt.xticks(range(0, 35, 7), aasd, rotation=0)
font1 = {'family': 'Times New Roman', 'weight': 'normal', 'size': 20}
ax.legend(loc=0, prop=font1)
font2 = {'family': 'Times New Roman', 'weight': 'normal', 'size': 25}
plt.axis('tight')
plt.xlabel('Date', font2)
plt.ylabel('Daily Infected Cases', font2)
plt.tick_params(labelsize=20)
plt.tight_layout()
plt.title('(d)', font2)

ax = fig.add_subplot(426)
ax = plt.gca()
ma7 = moving_average(coba_pre, 7, 'simple')
ax.plot(coba_pre[6:36], label='Prediction in Bay Area', marker="^", markersize=15, lw=4, color='deepskyblue')
ax.plot(ma7[6:36], label='7-days moving average', marker="s", markersize=15, lw=4, color='salmon')
aasd = ['06-21', '06-28', '07-05', '07-12', '07-19']
plt.xticks(range(0, 35, 7), aasd, rotation=0)
font1 = {'family': 'Times New Roman', 'weight': 'normal', 'size': 20}
ax.legend(loc=0, prop=font1)
font2 = {'family': 'Times New Roman', 'weight': 'normal', 'size': 25}
plt.axis('tight')
plt.xlabel('Date', font2)
plt.ylabel('Daily Infected Cases', font2)
plt.tick_params(labelsize=20)
plt.tight_layout()
plt.title('(f)', font2)

ax = fig.add_subplot(428)
ax = plt.gca()
ma7 = moving_average(cosd_pre, 7, 'simple')
ax.plot(cosd_pre[6:36], label='Prediction in San Diego/Imperial', marker="^", markersize=15, lw=4, color='deepskyblue')
ax.plot(ma7[6:36], label='7-days moving average', marker="s", markersize=15, lw=4, color='salmon')
aasd = ['06-21', '06-28', '07-05', '07-12', '07-19']
plt.xticks(range(0, 35, 7), aasd, rotation=0)
font1 = {'family': 'Times New Roman', 'weight': 'normal', 'size': 20}
ax.legend(loc=2, prop=font1)
font2 = {'family': 'Times New Roman', 'weight': 'normal', 'size': 25}
plt.axis('tight')
plt.xlabel('Date', font2)
plt.ylabel('Daily Infected Cases', font2)
plt.tick_params(labelsize=20)
plt.tight_layout()
plt.title('(h)', font2)

# plt.subplot(322)
# start = datetime.datetime(2020, 7, 4)
# stop = datetime.datetime(2020, 7, 17)
# days = datetime.timedelta(13)  # 10天
# delta = datetime.timedelta(1)  # 设定日期的间隔
# dates = mpl.dates.drange(start, stop, delta)
# ax = plt.gca()
# ax.plot(dates, tfla_pre, label='Prediction', marker="^", markersize=15, lw=4, color='coral')
# ax.plot(dates, tfla_gt, label='Ground Truth', marker="o", markersize=15, lw=4, color='deeppink')
# date_format = mpl.dates.DateFormatter('%m-%d')
# ax.xaxis.set_major_formatter(date_format)
# font1 = {'family': 'Times New Roman', 'weight': 'normal', 'size': 20}
# ax.legend(loc=4, prop=font1)
# #ax1.legend(loc=0, prop=font1)
# font2 = {'family': 'Times New Roman', 'weight': 'normal', 'size': 25}
# plt.axis('tight')
# plt.xticks(dates, rotation=45)
# plt.xlabel('Date', font2)
# plt.ylabel('Total Flow', font2)
# plt.tick_params(labelsize=20)
# plt.yticks(range(20000, 51000, 10000))
# plt.tight_layout()
# plt.title('(d)', font2)

#


plt.show()