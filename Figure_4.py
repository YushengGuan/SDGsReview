import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib as mpl
from Figure_1 import split_name
from Figure_2 import split_Q1
from adjustText import adjust_text


plt.rcParams['font.family'] = ['Arial']


def split_Q17(names):
    names = str(names)
    if '-' in names:
        names = names.split('-')
    if len(names) == 2 and len(str(names[0])) == 4 and len(str(names[1])) == 4:
        out = list(range(int(names[0]), int(names[1]) + 1))
        return out
    elif len(names) == 4:
        try:
            out = [int(names)]
        except Exception as e:
            out = -1
        return out
    else:
        return -1


def find_top(cols, number=10):
    from collections import Counter

    counter = Counter(cols)
    return counter.most_common(number)


if __name__ == '__main__':
    df = pd.read_excel(r'Included/影响评估_included_zh.xlsx')
    fig = plt.figure(figsize=(9, 9))
    
    beutblue = mpl.colors.LinearSegmentedColormap.from_list('beutblue', 
                                             [(0,    '#ffffff'),
                                                     (1,    '#2C73D2')], N=256)
    bins = [0, 1, 4, 16, 64, 256, 1024]
    
    methods = ['理论', '专家', '访谈', '案例', '文本',
               '指标', '聚类', '层次', '多准则', '遥感', 'GIS',
               '问卷', '统计', '回归', '结构方程', '机器学习',
               '系统动力', '投入产出', '均衡模型', 'ABM', '综合评估',
               '其它']
    method_names = ['Theoretical', 'Expert', 'Interview', 'Case', 'Text',
                    'Indicator', 'Clustering', 'Hierachical', 'Multilayer', 'Remote sensing', 'GIS',
                    'Questionnaire', 'Statics', 'Regression', 'SEM', 'ML',
                    'SD', 'I/O', 'Equilibrium', 'ABM', 'IAM',
                    'Others']
    df_draw = pd.DataFrame([[0]*17 for _ in range(len(methods))])

    for i in df.index:
        Q1 = split_Q1(df.loc[i, 'Q1'])
        Q14 = df.loc[i, 'Q14']
        try:
            flg = 0
            for j, m in enumerate(methods[:-1]):
                if m in Q14:
                    flg = 1
                    for item1 in Q1:
                        df_draw.loc[j, int(item1)-1] += 1
            if flg == 0:
                for item1 in Q1:
                    df_draw.loc[21, int(item1)-1] += 1
        except Exception as e:
            print(i, e)
    df_draw_log = np.log2(df_draw + 1)

    ax1 = fig.add_axes([0.1, 0.05, 0.9, 0.9])
    im = ax1.imshow(df_draw_log, interpolation='nearest', cmap=beutblue, vmin=0, vmax=10)
    ax1.set_xticks(np.linspace(0, 16, 17), [str(_) for _ in range(1, 18)])
    ax1.set_yticks(np.linspace(0, 21, 22), method_names)
    ax1.set_xlabel('SDG')
    ax1.text(-5.5, 10, 'Method', rotation=90, va='center', ha='center')
    
    for i in range(df_draw.shape[0]):
        for j in range(df_draw.shape[1]):
            if df_draw.loc[i, j] != 0:
                text = ax1.text(j, i, df_draw.loc[i, j],
                               ha="center", va="center", color="black", fontsize=10)
    cbar = fig.colorbar(im, ax=ax1, label='Number of articles',orientation='horizontal',location='top',fraction=0.02,pad=0.04,anchor=(0.5, 1))
    cbar.set_ticks(list(range(11)))
    cbar.set_ticklabels([2**_ for _ in range(11)])



    ax1.annotate('Qualitive', xy=(-0.2, 0.88), xytext=(-0.25,0.88), xycoords='axes fraction', 
                ha='center', va='center',rotation=90,
                arrowprops=dict(arrowstyle='-[, widthB=5, lengthB=0.5', lw=1))
    ax1.annotate('Indicator based', xy=(-0.2, 0.68), xytext=(-0.25,0.68), xycoords='axes fraction', 
                ha='center', va='center',rotation=90,
                arrowprops=dict(arrowstyle='-[, widthB=4.8, lengthB=0.5', lw=1))
    ax1.annotate('Data based', xy=(-0.2, 0.42), xytext=(-0.25,0.42), xycoords='axes fraction', 
                ha='center', va='center',rotation=90,
                arrowprops=dict(arrowstyle='-[, widthB=8, lengthB=0.5', lw=1))
    ax1.annotate('Model based', xy=(-0.2, 0.15), xytext=(-0.25,0.15), xycoords='axes fraction', 
                ha='center', va='center',rotation=90,
                arrowprops=dict(arrowstyle='-[, widthB=5.5, lengthB=0.5', lw=1))

    plt.savefig(r'Figs/Figure_4_a.png', dpi=300)

    fig = plt.figure(figsize=(4, 4))
    ax2 = fig.add_axes([0.16, 0.12, 0.7, 0.8])

    df_draw = pd.DataFrame([[0]*11 for _ in range(36)])  # model year vs publication year
    for i in df.index:
        Q17 = split_Q17(df.loc[i, 'Q17'])
        pub_year = df.loc[i, 'Publication Year']
        if Q17 != -1:
            mid_t = int(np.median(Q17))
            if 2005 <= mid_t <= 2040 and 2015 <= pub_year <= 2025:
                df_draw.loc[mid_t-2005, pub_year-2015] += 1
    df_draw_log = np.log2(df_draw)
    
    im = ax2.imshow(df_draw_log, interpolation='nearest', cmap=beutblue, aspect='auto', vmin=0, vmax=6)
    ax2.set_xticks(np.linspace(0, 10, 6), [str(_) for _ in range(2015, 2026, 2)])
    ax2.set_yticks(np.linspace(0, 35, 8), [str(_) for _ in range(2005, 2041, 5)])
    ax2.set_xlabel('Publication year')
    ax2.set_ylabel('Research period median year')
    
    ax2.plot([-0.5, 10.5], [9.5, 20.5], color='k')
    ax2.text(1, 15, 'lag = 0')
    ax2.plot([-0.5, 10.5], [5.5, 16.5], color='k')
    ax2.text(5, 8, 'lag = 4 years')
    ax2.set_xlim(-0.5, 10.5)
    ax2.set_ylim(-0.5, 35.5)

    cbar = fig.colorbar(im, ax=ax2, label='Number of articles',location='right',fraction=0.02,pad=0.04,anchor=(0.5, 1))
    cbar.set_ticks(list(range(7)))
    cbar.set_ticklabels([2**_ for _ in range(7)])
    plt.savefig(r'Figs/Figure_4_b.png', dpi=300)

    fig = plt.figure(figsize=(4, 4))
    ax3 = fig.add_axes([0.16, 0.12, 0.7, 0.8])
    scale = ['全球', '区域', '国', '省', '市', '县', '乡', '社区']
    scale_names = ['Global', 'Regional', 'Country', 'Provincial', 'City', 'County', 'Village', 'Community']
    df_draw = pd.DataFrame([[0]*11 for _ in range(len(scale))])
    for i in df.index:
        pub_year = df.loc[i, 'Publication Year']
        Q16 = df.loc[i, 'Q16']
        for j, s in enumerate(scale):
            if s in Q16 and 2015 <= pub_year <= 2025:
                df_draw.loc[j, pub_year-2015] += 1

    bottom = np.array([0]*11)
    for i in df_draw.index:
        print(df_draw.loc[i, :].values)
        ax3.bar(np.linspace(0, 10, 11), df_draw.loc[i, :].values, bottom=bottom, width=0.8, label=scale_names[i])
        bottom += df_draw.loc[i, :].values
    ax3.legend(loc='upper left', frameon=False)
    ax3.set_xticks(np.linspace(0, 10, 6), [str(_) for _ in range(2015, 2026, 2)])
    ax3.set_xlabel('Publication year')
    ax3.set_ylabel('Number of articles')
    ax3.set_ylim(0, 800)
    plt.savefig(r'Figs/Figure_4_c.png', dpi=300)

    fig = plt.figure(figsize=(4, 4))
    ax4 = fig.add_axes([0.16, 0.12, 0.7, 0.8])
    span = ['年', '季度', '月', '周', '日', '时', '分钟', '秒']
    scale_names = ['Year', 'Season', 'Month', 'Week', 'Day', 'Hour', 'Minute', 'Second']
    df_draw = pd.DataFrame([[0] * 11 for _ in range(len(span))])
    for i in df.index:
        pub_year = df.loc[i, 'Publication Year']
        Q18 = str(df.loc[i, 'Q18'])
        for j, s in enumerate(span):
            if s in Q18 and 2015 <= pub_year <= 2025:
                df_draw.loc[j, pub_year - 2015] += 1

    bottom = np.array([0] * 11)
    for i in df_draw.index:
        ax4.bar(np.linspace(0, 10, 11), df_draw.loc[i, :].values, bottom=bottom, width=0.8, label=scale_names[i])
        bottom += df_draw.loc[i, :].values
    ax4.legend(loc='upper left', frameon=False)
    ax4.set_xticks(np.linspace(0, 10, 6), [str(_) for _ in range(2015, 2026, 2)])
    ax4.set_xlabel('Publication year')
    ax4.set_ylabel('Number of articles')
    ax4.set_ylim(0, 800)
    plt.savefig(r'Figs/Figure_4_d.png', dpi=300)

    fig = plt.figure(figsize=(6, 9))
    df_draw = pd.DataFrame([[0] * 11 for _ in range(len(methods))])
    for i in df.index:
        pub_year = df.loc[i, 'Publication Year']
        Q14 = df.loc[i, 'Q14']
        try:
            flg = 0
            for j, m in enumerate(methods[:-1]):
                if m in Q14 and 2015 <= pub_year <= 2025:
                    flg = 1
                    df_draw.loc[j, pub_year - 2015] += 1
            if flg == 0:
                df_draw.loc[21, pub_year - 2015] += 1
        except Exception as e:
            print(i, e)
    df_draw_log = np.log2(df_draw + 1)

    ax5 = fig.add_axes([0.1, 0.05, 0.9, 0.9])
    im = ax5.imshow(df_draw_log, interpolation='nearest', cmap=beutblue, vmin=0, vmax=10)
    ax5.set_xticks(np.linspace(0, 10, 11), [str(_) for _ in range(2015, 2026, 1)])
    ax5.set_yticks(np.linspace(0, 21, 22), method_names)
    ax5.set_xlabel('Publication year')
    ax5.set_ylabel('Method')

    for i in range(df_draw.shape[0]):
        for j in range(df_draw.shape[1]):
            if df_draw.loc[i, j] != 0:
                text = ax5.text(j, i, df_draw.loc[i, j],
                                ha="center", va="center", color="black", fontsize=10)
    cbar = fig.colorbar(im, ax=ax5, label='Number of articles', orientation='horizontal', location='top',
                        fraction=0.02, pad=0.04, anchor=(0.5, 1))
    cbar.set_ticks(list(range(11)))
    cbar.set_ticklabels([2 ** _ for _ in range(11)])

    plt.savefig(r'Figs/Figure_4_e.png', dpi=300)

    fig = plt.figure(figsize=(9, 4))
    ax6 = fig.add_axes([0.1, 0.05, 0.85, 0.9])
    df_region = pd.read_excel(r'worldmap_gaode/country.xlsx')
    region20 = find_top(df.loc[:, 'Q15'].values, 20)

    region20[0] = ('全球', 594-200)  # broken ax

    gdp_pop = [0] * 20
    for j, value in enumerate(region20):
        if value[0] not in ['非洲', '欧洲', '全球']:
            gdp_pop[j] = float(df_region.loc[df_region['中文名']==value[0], '人均GDP'] / 100)
    gdp_pop[0] = 134.16
    gdp_pop[14] = 19.40
    gdp_pop[15] = 537.83

    names = [''] * 20
    for j, value in enumerate(region20):
        if value[0] not in ['非洲', '欧洲', '全球']:
            names[j] = str(df_region.loc[df_region['中文名']==value[0], 'region'].values[0])
    names[0] = 'Global'
    names[14] = 'Africa'
    names[15] = 'Europe'

    color = ['Steelblue']*20
    for j, value in enumerate(region20):
        if value[0] not in ['非洲', '欧洲', '全球']:
            if str(df_region.loc[df_region['中文名'] == value[0], 'type'].values[0]) == 'Developing':
                color[j] = "orange"
            elif str(df_region.loc[df_region['中文名'] == value[0], 'type'].values[0]) == 'Developed':
                color[j] = "green"

    ax6.bar(np.linspace(1, 20, 20), [v for s, v in region20], color='grey', width=0.05)
    # for j in range(20):
    #     ax6.scatter(j+1, region20[j][1], color=color[j], s=gdp_pop[j])
    scatter = ax6.scatter(np.linspace(1, 20, 20), [v for s, v in region20], color=color, s=gdp_pop)
    texts = []
    for j in range(20):
        texts.append(ax6.text(j+1.1, region20[j][1], names[j], fontsize=10))
    adjust_text(texts, arrowprops=dict(arrowstyle='->', color='black'))
    ax6.set_xticks([], [])
    ax6.set_ylabel('Number of articles')

    ax6.set_yticks([0, 50, 100, 150, 200, 250, 350, 400], [0, 50, 100, 150, 200, 250, 550, 600])


    # 创建图例
    # 为了创建大小图例，我们需要创建一些带有特定大小的散点，并添加到图例中
    size_labels = [10, 50, 100, 300, 500]  # 假设的大小标签
    size_label_names = ['1,000', '5,000', '10,000', '30,000', '50,000']
    handles = []
    for size in size_labels:
        handles.append(plt.scatter([], [], color='grey', s=size))
    legend1 = ax6.legend(handles, size_label_names, title="Size: GDP per capita ($)", scatterpoints=1, frameon=False, labelspacing=1.5,
                        handlelength=2)
    color_labels = ['Developing', 'Developed', 'Region']
    handles = []
    for j, c in enumerate(color_labels):
        handles.append(plt.scatter([], [], color=['orange', 'green', 'steelblue'][j], s=100))
    legend2 = ax6.legend(handles, color_labels, title="Color: Type", scatterpoints=1, frameon=False,
                         labelspacing=1.5,
                         handlelength=2, bbox_to_anchor=(0.8, 1))

    # 将大小图例添加到图表中
    ax6.add_artist(legend1)
    ax6.add_artist(legend2)
    plt.savefig(r'Figs/Figure_4_f.png', dpi=300)

    

