import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.font_manager as fm
import numpy as np


# 讀取資料
# dataSource_pd = pd.read_csv("Element/台灣電力公司_各縣市住宅、服務業及機關用電統計資料.csv")
dataSource_pd = pd.read_csv("Element/新增資料後的檔案.csv")


# 各縣市 (住宅, 服務, 農林漁牧, 工業部門用電)

#------------------------
# residential_pw : 住宅用電
# service_pw : 服務用電  
# AFFA_pw : 農林漁牧用電
# industry_pw : 工業用電
#------------------------

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
labelColor = {'color':'darkred', 'size': 14, 'weight':'bold'}

# 設定資料
# 2021 4月 各縣市用電量長條圖 (x: 各個縣市, y:用量(單位度), legend: 顯示四個項目)
residential_pw = dataSource_pd.loc[0:21, '住宅部門售電量(度)']
service_pw = dataSource_pd.loc[0:21, '服務業部門(含包燈)(度)']
AFFA_pw = dataSource_pd.loc[0:21, '農林漁牧售電量(度)']
industry_pw = dataSource_pd.loc[0:21, '工業部門售電量(度)']


# 把上面的單位 換成( 百萬度 )
newResidential_pw = [i/1000000 for i in residential_pw]
newService_pw = [i/1000000 for i in service_pw]
newAFFA_pw = [i/1000000 for i in AFFA_pw]
newIndustry_pw = [i/1000000 for i in industry_pw]


areas = [ '新北市', '台北市', '桃園市', '台中市', '台南市', '高雄市', '宜蘭縣', '新竹縣', '苗栗縣', '彰化縣', '南投縣', '雲林縣', '嘉義縣', '屏東縣', '台東縣', '花蓮縣', '基隆市', '新竹市', '嘉義市', '澎湖縣', '金門縣', '連江縣']

labelCount = np.arange(len(areas))
# print(labelCount)
barWidth = 0.2

# 將資料帶入圖表
fig, ax = plt.subplots(figsize=(14, 8), num="各縣市用電量")
ax.bar(labelCount - barWidth*2, newResidential_pw, barWidth, color="olive", label='住宅用電')
ax.bar(labelCount - barWidth, newService_pw, barWidth, color="darkorange", label='服務業用電')
ax.bar(labelCount, newAFFA_pw, barWidth, color="crimson", label='農林漁牧')
ax.bar(labelCount + barWidth, newIndustry_pw, barWidth, color="steelblue", label='工業部門用電')


# fix the x-axes
ax.set_xticks(labelCount - barWidth/2)
ax.set_xticklabels(areas, fontsize='8')

# Add legend
ax.legend(shadow=True, fancybox=True)

# Axis styling
# 把圖片預設的框框給去掉
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_color('#DDDDDD')

ax.tick_params(bottom=False, left=False)
ax.set_axisbelow(True)
ax.yaxis.grid(True, color="#EEEEEE")
ax.xaxis.grid(False)

ax.set_ylabel("台電售電量(百萬度)", fontdict=labelColor, labelpad=20)


ax.set_title("台電 2021年 4月 各縣市售電量")


# ------------------------------------------------------------------------------
### 這段code 可以讓你長條圖的數字顯示在上面
# # For each bar in the chart, add a text label.
# for bar in ax.patches:
#   # The text annotation for each bar should be its height.
#   bar_value = bar.get_height()
#   # Format the text with commas to separate thousands. You can do
#   # any type of formatting here though.
#   text = f'{bar_value:,}'
#   # This will give the middle of each bar on the x-axis.
#   text_x = bar.get_x() + bar.get_width() / 2
#   # get_y() is where the bar starts so we add the height to it.
#   text_y = bar.get_y() + bar_value
#   # If we want the text to be the same color as the bar, we can
#   # get the color like so:
#   bar_color = bar.get_facecolor()
#   # If you want a consistent color, you can just set it as a constant, e.g. #222222
#   ax.text(text_x, text_y, text, ha='center', va='bottom', color=bar_color, size=12)### 繪製成圖
# ------------------------------------------------------------------------------



### ----- 2020 和 2021 1到6月份的住宅用電量比較 -------

# 使用groupby 把 "合計" 的資料給擷取出來
groupData = dataSource_pd.groupby("縣市")
totalPowerList = groupData.get_group("合計")  # 合計的資料
# print(totalPowerList)

# 再把資料的index 換成 日期
totalPowerList.set_index("日期", inplace=True)
# print(totalPowerList)

### ----- 2020 和 2021 1到6月份的工業用電量比較 -------

# 取出我們的 2020 跟 2021 1~6 月的總售電量
total2019_pw = totalPowerList.loc['2019年06月':'2019年01月', '工業部門售電量(度)']
total2020_pw = totalPowerList.loc['2020年06月':'2020年01月', '工業部門售電量(度)']
total2021_pw = totalPowerList.loc['2021年06月':'2021年01月', '工業部門售電量(度)']
# print(total2020_pw)

# 把我要的資料從 Series資料形態中取出
total2019_pw_list = [i / 1000000 for i in total2019_pw.values]
total2020_pw_list = [i / 1000000 for i in total2020_pw.values]
total2021_pw_list = [i / 1000000 for i in total2021_pw.values]
# print(total2021_pw_list)

### 開始繪出圖形
# 設定資料
x = np.arange(len(total2020_pw_list))
print(x)
xlabels = [str(i)+'月' for i in range(1, len(total2020_pw_list)+1)]
print(xlabels)
barWidth2 = 0.15

# 把資料帶入圖表
# plt.figure()  # 創建新的畫布
fig, ax = plt.subplots()

ax.bar(x - barWidth2, total2019_pw_list, barWidth2, label="2019年 每月工業用電量", color="indianred")
ax.bar(x, total2020_pw_list, barWidth2, label="2020年 每月工業用電量", color="wheat")
ax.bar(x + barWidth2, total2021_pw_list, barWidth2, label="2021年 每月工業用電量", color="olivedrab")

# fix x-axis
ax.set_xticks(x)
ax.set_xticklabels(xlabels)
# ax.set_ylim(0, 6500)

# Add legend
fig.legend(shadow=True, fancybox=True)

# Axis style 
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_color('#DDDDDD')

ax.tick_params(bottom=False, left=False)
ax.set_axisbelow(True)
ax.yaxis.grid(True, color="#EEEEEE")
ax.xaxis.grid(False)

ax.set_ylabel("台電售電量(百萬度)", fontdict=labelColor, labelpad=20)
fig.suptitle("2019~2021年 - 1到6月份的工業用電量比較")


# --------------------------------------------------------------------------

### ----- 2020 和 2021 1到6月份的服務業用電量比較 -------

# 取出我們的 2020 跟 2021 1~6 月的總售電量
total2019_pw = totalPowerList.loc['2019年06月':'2019年01月', '服務業部門(含包燈)(度)']
total2020_pw = totalPowerList.loc['2020年06月':'2020年01月', '服務業部門(含包燈)(度)']
total2021_pw = totalPowerList.loc['2021年06月':'2021年01月', '服務業部門(含包燈)(度)']
# print(total2020_pw)

# 把我要的資料從 Series資料形態中取出
total2019_pw_list = [i / 1000000 for i in total2019_pw.values]
total2020_pw_list = [i / 1000000 for i in total2020_pw.values]
total2021_pw_list = [i / 1000000 for i in total2021_pw.values]
# print(total2021_pw_list)

### 開始繪出圖形
# 設定資料
x = np.arange(len(total2020_pw_list))
print(x)
xlabels = [str(i)+'月' for i in range(1, len(total2020_pw_list)+1)]
print(xlabels)
barWidth2 = 0.15

# 把資料帶入圖表
# plt.figure()  # 創建新的畫布
fig, ax = plt.subplots()

ax.bar(x - barWidth2, total2019_pw_list, barWidth2, label="2019年 每月服務業用電量", color="indianred")
ax.bar(x, total2020_pw_list, barWidth2, label="2020年 每月服務業用電量", color="wheat")
ax.bar(x + barWidth2, total2021_pw_list, barWidth2, label="2021年 每月服務業用電量", color="olivedrab")

# fix x-axis
ax.set_xticks(x)
ax.set_xticklabels(xlabels)
# ax.set_ylim(0, 6500)

# Add legend
fig.legend(shadow=True, fancybox=True)

# Axis style 
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_color('#DDDDDD')

ax.tick_params(bottom=False, left=False)
ax.set_axisbelow(True)
ax.yaxis.grid(True, color="#EEEEEE")
ax.xaxis.grid(False)

ax.set_ylabel("台電售電量(百萬度)", fontdict=labelColor, labelpad=20)
fig.suptitle("2019~2021年 - 1到6月份的服務業用電量比較")

plt.show()
