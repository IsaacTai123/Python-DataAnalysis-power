import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

# 讀取資料
dataSource_pd = pd.read_csv('Element/台灣電力公司_過去電力供需資訊.csv')

# 把index 換成日期
dataSource_pd.set_index('日期', inplace=True)

# 把資料 "備轉容量率(%)" 取出來
get2020_may = dataSource_pd.loc['20200501':'20200531', '備轉容量率(%)'].values
get2021_may = dataSource_pd.loc['20210501':'20210531', '備轉容量率(%)'].values

### 把資料繪製成圖
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
labelColor = {'color':'darkred', 'size': 14}


# 設定資料
# x = [i for i in range(1, 32)]
# x = np.arange(31)
xlabels = [str(i) for i in range(1, 32)]

# 把資料帶入圖片
fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(xlabels, get2020_may, color="firebrick", marker='o', linestyle='-', label="2020年 五月份")
ax.plot(xlabels, get2021_may, color="steelblue",  marker='o', linestyle='-', label="2021年 五月份")

# 設定x軸的中文字
ax.set_ylim(0, 18)
ax.set_xlim(0, 31)
# ax.set_xticklabels(xlabels)

# Add legend
ax.legend(shadow=True, fancybox=True)

# Axis style
ax.xaxis.grid(True, color="#EEEEEE")
ax.yaxis.grid(True, color="#EEEEEE")
ax.set_xlabel("日期(號)", fontdict=labelColor, labelpad=10)
ax.set_ylabel("備轉容量率(%)", fontdict=labelColor, labelpad=20)
ax.set_title("2021年 - 備轉容量率")

# 試著把數字帶入長條圖 或是其他圖
for x,y in enumerate(get2020_may):  # 使用enumerate的原因是他可以一次loop through兩個(數字 跟 變數)
    # plt.text(x,y, "{:.1f}%".format(y), ha='center', va='bottom')
    plt.text(x,y, "{:.1f}%".format(y), va='top')

plt.show()
