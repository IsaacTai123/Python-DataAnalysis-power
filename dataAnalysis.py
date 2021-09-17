## 台灣各個發電廠歷年的發電狀況變化 
# 讀取csv 檔案
import csv
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
from matplotlib.gridspec import GridSpec

# 把外部檔案讀進來 "powerFile": 發電資料

## 使用Pandas 把外部檔案讀進來 "powerFile": 發電資料
powerFile_df = pd.read_csv('Element/經濟部能源局_發電量統計表(年)(094-109)(110版).csv')

indexList = [i for i in range(94, 110)]
# print(powerFile_df)
# print(powerFile_df.set_index('日期(年度)'))
powerFile_df.set_index(pd.Index(indexList), '日期(年度)', inplace=True)  # 更改DataFrame裡面的index 設為 "日期(年度)"
print(powerFile_df.head())



#------------------
# date 日期
# water_g 水力發電
# fire_g 火力發電
# nuclear_g 核能發電
# regenerat_g 再生發電
#------------------


###  繪製圖表
# 先設定matplotlib 讓其可以顯示中文
plt.rcParams['font.family'] = "microsoft yahei"
plt.rcParams['font.size'] = 12

# fontPath = 'c:\windows\fonts\mingliu.ttc'  # 這是windows的
fontPath = '/home/isaac/.local/share/fonts/kaiu.ttf'  # 這是Linux 裡面的路徑 
fontProp = fm.FontProperties(fname=fontPath)
fontProp.set_size('12')
fontProp.set_style('normal')

fontColor = {'color':'darkred', 'size': 12}
titleColor = {'color':'brown'}
labelColor = {'color':'darkred'}

# ---- 四大主要發電量圓餅圖 ----
## 設定資料並且帶入圖表
power_100 = [
        powerFile_df.loc[100, '抽蓄水力'], 
        powerFile_df.loc[100, '火力'], 
        powerFile_df.loc[100, '核能'], 
        powerFile_df.loc[100, '再生能源'] 
        ]   # 100年的各項發電量

power_109 = [
        powerFile_df.loc[109, '抽蓄水力'], 
        powerFile_df.loc[109, '火力'], 
        powerFile_df.loc[109, '核能'], 
        powerFile_df.loc[109, '再生能源'] 
        ]   # 109年的各項發電量


labelName = ['抽蓄水力', '火力', '核能', '再生能源']
explode = [0.1, 0, 0.1, 0.15]
colors = ['lightblue', 'red', 'yellow', 'lightgreen']


# 分割多圖
fig, ax = plt.subplots(1, 2, figsize=(15,8), num='台灣主要發電量分布圖')


# 設定第一張子圖
ax[0].pie(power_100, labels=labelName, shadow=True, explode=explode, colors=colors, autopct="%.1f%%")
# 設定第二張子圖
ax[1].pie(power_109, labels=labelName, shadow=True, explode=explode, colors=colors, autopct="%.1f%%")
plt.legend(loc='best', shadow=True, fancybox=True)

## 圖表的相關設定
ax[0].set_xlabel("民國100年台灣四大主要發電量", fontdict=labelColor)
ax[1].set_xlabel("民國109年台灣四大主要發電量", fontdict=labelColor)
# fig.legend(shadow=True, fancybox=True)  #設定圖例

fig.suptitle("100跟109年 - 台灣四大主要發電量占比", fontweight="bold")
fig.tight_layout()



# ---- 火力, 水力, 核能, 再生能 歷年發電的曲線變化 ----

## 設定資料並帶入圖表

# 把資料從2維的DataFrame 裡面讀出來 "用Series的屬性values 把資料取出"
date = powerFile_df['日期(年度)'].values
water_g = powerFile_df['抽蓄水力'].values
fire_g = powerFile_df['火力'].values
nuclear_g = powerFile_df['核能'].values
regenerate_g = powerFile_df['再生能源'].values

# 分割多圖
fig, ax = plt.subplots(2, 2, figsize=(14, 8), num='四大發電歷年發電曲線圖')

ax[0, 0].plot(date, water_g, '-', label='抽蓄水力')
ax[0, 1].plot(date, fire_g, 'r-', label='火力')
ax[1, 0].plot(date, nuclear_g, 'y-', label='核能')
ax[1, 1].plot(date, regenerate_g, 'g-', label='再生能源')

ax[0, 0].legend(shadow=True, fancybox=True)
ax[0, 1].legend(shadow=True, fancybox=True)
ax[1, 0].legend(shadow=True, fancybox=True)
ax[1, 1].legend(shadow=True, fancybox=True)

ax[0, 0].grid()
ax[0, 1].grid()
ax[1, 0].grid()
ax[1, 1].grid()
fig.suptitle('台灣主要四大發電 - 歷年發電量變化')
fig.text(0.5, 0.04, '單位(年)', fontdict=labelColor,  horizontalalignment='center', verticalalignment='center')
fig.text(0.06, 0.5, '單位(百萬度)',fontdict=labelColor, horizontalalignment='center', verticalalignment='center', rotation='vertical')


# plt.figure()
# fig, ax = plt.subplots(4, 1, num='四大發電歷年發電曲線圖', sharex=True)
# labels = ['火力', '核能', '再生能源', '抽蓄水力']
# colors = ['r-', 'y-', 'g-', '-']
# yaxis = [fire_g, nuclear_g, regenerate_g, water_g]
#
# for i in range(4):
#     print(i)
#     ax[i].plot(date, yaxis[i], colors[i], label=labels[i])
#     ax[i].legend(loc='upper left')

# fig.suptitle('四大發電歷年發電曲線圖')
# fig.add_subplot(111, frame_on=False)
# plt.tick_params(labelcolor="none", top=False, bottom=False, left=False, right=False)
# plt.xlabel("單位(年)", fontdict=labelColor)
# plt.ylabel("單位(百萬度)", labelpad=30, fontdict=labelColor)


# ---- 台電再生能源的分布 ----

# ---------------------
# regen_person : 再生能源-自用發電設備
# regen_private : 再生能源-民營
# regen_pub : 再生能源-台電
# ---------------------
regen_pub = powerFile_df.loc[94:, '再生能源_台電']
regen_private = powerFile_df.loc[94:, '再生能源_民營電廠']
regen_person = powerFile_df.loc[94:, '再生能源_自用發電設備']

## 再生能源台電的變化

# 設定資料並帶入圖表
regen_100 = [
        powerFile_df.loc[108, '再生能源_台電_慣常水力'],
        powerFile_df.loc[108, '再生能源_台電_太陽光電'],
        powerFile_df.loc[108, '再生能源_台電_風力']
        ]
regen_109 = [
        powerFile_df.loc[109, '再生能源_台電_慣常水力'],
        powerFile_df.loc[109, '再生能源_台電_太陽光電'],
        powerFile_df.loc[109, '再生能源_台電_風力']
        ]

labelName2 = ['慣常水利', '太陽光電', '風力']
colors2 = ['steelblue', 'orange', 'gainsboro']
explode2 = [0.1, 0.1, 0.05]


fig, ax = plt.subplots(1, 2, figsize=(14, 8), num="再生能源分布圖")
ax[0].pie(regen_100, labels=labelName2, colors=colors2, explode=explode2, startangle=70, shadow=True, autopct='%.1f%%')
ax[1].pie(regen_109, labels=labelName2, colors=colors2, explode=explode2, startangle=70, shadow=True, autopct='%.1f%%')


ax[1].legend(loc='upper right', shadow=True, fancybox=True)
ax[0].set_xlabel('108年', fontdict=labelColor)
ax[1].set_xlabel('109年', fontdict=labelColor)
fig.suptitle("108跟109年 - 台電再生能源的分布")


# ---- 再生能源中 慣常水利的發電狀況(台電&民營) ----

## regen_water : 再生能源_慣常水利
regen_water = powerFile_df.loc[94:, '再生能源_台電_慣常水力']

fig, ax = plt.subplots(num = '慣常水力')
ax.bar(date, regen_water, label='台電-慣常水力', width=0.5, align='center', color="skyblue")
ax.legend(shadow=True, fancybox=True)
ax.set_xlabel("單位(年)", fontdict=labelColor, labelpad=10)
ax.set_ylabel("單位(百萬度)", fontdict=labelColor, labelpad=20)
ax.set_title("台電慣常水力-歷年來變化")

# Axis style 
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_color('#DDDDDD')

ax.tick_params(bottom=False, left=False)
ax.set_axisbelow(True)
ax.yaxis.grid(True, color="#EEEEEE")
ax.xaxis.grid(False)


# ---- 再生能源中 再生能源_自用發電設備_太陽光的發電狀況(民營) ----

## regen_water : 再生能源_慣常水利
regen_water = powerFile_df.loc[94:, '再生能源_自用發電設備_太陽光電']

fig, ax = plt.subplots()
ax.bar(date, regen_water, label='再生能源_自用發電設備_太陽光電', width=0.5, align='center', color="gold")
# ax.legend(shadow=True, fancybox=True)
ax.set_xlabel("單位(年)", fontdict=labelColor, labelpad=10)
ax.set_ylabel("單位(百萬度)", fontdict=labelColor, labelpad=20)
ax.set_title("再生能源_自用發電設備_太陽光電 - 歷年來變化")

# Axis style 
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_color('#DDDDDD')

ax.tick_params(bottom=False, left=False)
ax.set_axisbelow(True)
ax.yaxis.grid(True, color="#EEEEEE")
ax.xaxis.grid(False)



plt.show()
