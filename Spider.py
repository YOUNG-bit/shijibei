
'''
在这部分要分阶段展示同学们在不同时间段的需求变化
希望可以以蜘蛛网图的呈现方式进行呈现
主要的需求有生活、学业、社交、心理、求职这五大方面
最终展示的图是北理工在2019年从1月到12月我们公众号收集上来的数据并进行综合分析的结果
由于数据来源保密，但是其中设计将词语进行聚类分析的算法，
主要是用spss软件来实现

'''

#Import libs
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

def get_spider():
    # Get the data
    df = pd.read_csv("doc/spider.csv")
    print(df)

    """
       #             Name  Attack  Defense  Speed  Range  Health
    0  1         Iron Man      83       80     75     70      70
    1  2  Captain America      60       62     63     80      80
    2  3             Thor      80       82     83    100     100
    3  3             Hulk      80      100     67     44      92
    4  4      Black Widow      52       43     60     50      65
    5  5          Hawkeye      58       64     58     80      65

    """

    # Get the data for Iron Man
    for i in range(6):
        labels = np.array(['Life','School','Social','Mental','Job'])
        stats = df.loc[i, labels].values

        # Make some calculations for the plot

        angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False)
        stats = np.concatenate((stats, [stats[0]]))
        angles = np.concatenate((angles, [angles[0]]))
        labels = np.concatenate((labels, [labels[0]]))  # 对labels进行封闭
        # Plot stuff
        fig = plt.figure(i)
        ax = fig.add_subplot(111, polar=True)
        ax.plot(angles, stats, 'o-', linewidth=2)
        ax.fill(angles, stats, alpha=0.25)
        ax.set_thetagrids(angles * 180 / np.pi, labels)
        ax.set_title([df.loc[i, "time"]])
        ax.grid(True)

        plt.show()

get_spider()