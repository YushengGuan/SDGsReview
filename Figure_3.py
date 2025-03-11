import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib as mpl
from Figure_1 import split_name
from Figure_2 import split_Q1

plt.rcParams['font.family'] = ['Arial']


if __name__ == '__main__':
    df = pd.read_excel(r'Included/影响评估_included_zh.xlsx')

    beutblue = mpl.colors.LinearSegmentedColormap.from_list('beutblue', 
                                             [(0,    '#ffffff'),
                                                     (1,    '#9D3FB1')], N=256)
    bins = [0, 1, 4, 16, 64, 256, 1024]

    impacts = [['政府', '机构', '企业', '居民', '消费者'],
               ['年龄', '收入', '教育', '性别', '残疾', '地区', '城乡'],
               ['煤', '油', '气', '光', '风', '水', '生物', '核'],
               ['变化', '大气', '水', '土壤', '固体', '生物'],
    ]
    impact_names = [['Government', 'Institution', 'Company', 'Household', 'Consumer'],
                    ['Age', 'Income', 'Education', 'Gender', 'Disability', 'Region', 'Rural'],
                    ['Coal', 'Oil', 'Gas', 'Solar', 'Wind', 'Hydro', 'Biomass', 'Nuclear'],
                    ['Climate', 'Air', 'Water', 'Soil', 'Waste', 'Biodiversity'],
    ]
    Qs_i = ['Q6', 'Q10', 'Q7', 'Q8']
    Ls1 = [5, 7, 8, 6]
    df_draw = pd.DataFrame([[0]*17 for _ in range(sum(Ls1))])

    for i in df.index:
        Q1 = split_Q1(df.loc[i, 'Q1'])
        for k in range(len(impacts)):
            Q = df.loc[i, Qs_i[k]]
            try:
                for j, m in enumerate(impacts[k]):
                    if m in Q:
                        for item1 in Q1:
                            df_draw.loc[j+sum(Ls1[:k]), int(item1)-1] += 1
            except Exception as e:
                print(i, e)
    df_draw_log = np.log2(df_draw + 1)

    fig = plt.figure(figsize=[8, 10])
    ax1 = fig.add_axes([0.1, 0.05, 0.9, 0.9])
    im = ax1.imshow(df_draw_log, interpolation='nearest', cmap=beutblue, vmin=0, vmax=10)
    ax1.set_xticks(np.linspace(0, 16, 17), [str(_) for _ in range(1, 18)])
    ax1.set_yticks(np.linspace(0, 25, 26), [item for sublist in impact_names for item in sublist])
    ax1.set_xlabel('SDG')
    ax1.set_ylabel('Impacts')

    for i in range(df_draw.shape[0]):
        for j in range(df_draw.shape[1]):
            if df_draw.loc[i, j] != 0:
                text = ax1.text(j, i, df_draw.loc[i, j],
                               ha="center", va="center", color="black", fontsize=10)
    cbar = fig.colorbar(im, ax=ax1, label='Number of articles',orientation='horizontal',location='top',fraction=0.02,pad=0.04,anchor=(0.5, 1))
    cbar.set_ticks(list(range(11)))
    cbar.set_ticklabels([2**_ for _ in range(11)])

    plt.savefig(r'Figs/Figure_3_a.png', dpi=300)
    
    objects = [['教育', '公共管理', '卫生', '农', '环境', '制造', '建筑', '电力', '金融', '采矿', '文化', '交通', '信息', '跨行业'],
               ['可再生能源', 'CCS', 'AI', '数字', '车'],
               ['经济', '管理', '环境', '技术'],
               ['战争', '气候', 'COVID'],
    ]
    object_names = [['Education', 'Public Admin', 'Sanity', 'Agriculture', 'Environment', 'Manufacturing', 'Construction', 'Electricity', 'Finance', 'Mining', 'Culture', 'Transportation', 'Information', 'Cross-sector'],
                    ['Renewables', 'CCS', 'AI', 'Digital', 'Vehicles'],
                    ['Economic', 'Management', 'Environment', 'Technology'],
                    ['War', 'Extreme climate', 'COVID'],
    ]
    Qs_o = ['Q5', 'Q11', 'Q12', 'Q13']
    Ls2 = [14, 5, 4, 3]
    df_draw = pd.DataFrame([[0]*17 for _ in range(sum(Ls2))])

    for i in df.index:
        Q1 = split_Q1(df.loc[i, 'Q1'])
        for k in range(len(objects)):
            Q = df.loc[i, Qs_o[k]]
            try:
                for j, m in enumerate(objects[k]):
                    if m in Q:
                        for item1 in Q1:
                            df_draw.loc[j+sum(Ls2[:k]), int(item1)-1] += 1
            except Exception as e:
                print(i, e)
    df_draw_log = np.log2(df_draw + 1)

    fig = plt.figure(figsize=[8, 10])
    ax1 = fig.add_axes([0.1, 0.05, 0.9, 0.9])
    im = ax1.imshow(df_draw_log, interpolation='nearest', cmap=beutblue, vmin=0, vmax=10)
    ax1.set_xticks(np.linspace(0, 16, 17), [str(_) for _ in range(1, 18)])
    ax1.set_yticks(np.linspace(0, 25, 26), [item for sublist in object_names for item in sublist])
    ax1.set_xlabel('SDG')
    ax1.set_ylabel('Objects')

    for i in range(df_draw.shape[0]):
        for j in range(df_draw.shape[1]):
            if df_draw.loc[i, j] != 0:
                text = ax1.text(j, i, df_draw.loc[i, j],
                               ha="center", va="center", color="black", fontsize=10)
    cbar = fig.colorbar(im, ax=ax1, label='Number of articles',orientation='horizontal',location='top',fraction=0.02,pad=0.04,anchor=(0.5, 1))
    cbar.set_ticks(list(range(11)))
    cbar.set_ticklabels([2**_ for _ in range(11)])

    plt.savefig(r'Figs/Figure_3_b.png', dpi=300)
    
    beutblue = mpl.colors.LinearSegmentedColormap.from_list('beutblue', 
                                                     [(0,    '#ffffff'),
                                                             (1,    '#D7CA37')], N=256)
    
    df_draw = pd.DataFrame([[0]*sum(Ls2) for _ in range(sum(Ls1))])

    for i in df.index:
        for q in range(len(impacts)):
            Qi = str(df.loc[i, Qs_i[q]])
            for p in range(len(objects)):
                Qo = str(df.loc[i, Qs_o[p]])
                for j, m in enumerate(objects[p]):
                    for k, n in enumerate(impacts[q]):
                        if n in Qi and m in Qo:
                            df_draw.loc[k+sum(Ls1[:q]), j+sum(Ls2[:p])] += 1
    df_draw_log = np.log2(df_draw + 1)

    fig = plt.figure(figsize=[10, 10])
    ax1 = fig.add_axes([0.15, 0.15, 0.8, 0.8])
    im = ax1.imshow(df_draw_log, interpolation='nearest', cmap=beutblue, vmin=0, vmax=10)
    ax1.set_xticks(np.linspace(0, 25, 26), [item for sublist in object_names for item in sublist], rotation=90)
    ax1.set_yticks(np.linspace(0, 25, 26), [item for sublist in impact_names for item in sublist])

    for i in range(df_draw.shape[0]):
        for j in range(df_draw.shape[1]):
            if df_draw.loc[i, j] != 0:
                text = ax1.text(j, i, df_draw.loc[i, j],
                               ha="center", va="center", color="black", fontsize=10)
    cbar = fig.colorbar(im, ax=ax1, label='Number of articles',orientation='horizontal',location='top',fraction=0.02,pad=0.02,anchor=(0.5, 1))
    cbar.set_ticks(list(range(11)))
    cbar.set_ticklabels([2**_ for _ in range(11)])
    
    ax1.annotate('Economic', xy=(-0.13, 0.9), xytext=(-0.16,0.9), xycoords='axes fraction', 
                ha='center', va='center',rotation=90,
                arrowprops=dict(arrowstyle='-[, widthB=4.8, lengthB=0.5', lw=1))
    ax1.annotate('Social', xy=(-0.13, 0.67), xytext=(-0.16, 0.67), xycoords='axes fraction', 
                ha='center', va='center',rotation=90,
                arrowprops=dict(arrowstyle='-[, widthB=7, lengthB=0.5', lw=1))
    ax1.annotate('Energy', xy=(-0.13, 0.38), xytext=(-0.16, 0.38), xycoords='axes fraction', 
                ha='center', va='center',rotation=90,
                arrowprops=dict(arrowstyle='-[, widthB=7.8, lengthB=0.5', lw=1))
    ax1.annotate('Environment', xy=(-0.13, 0.11), xytext=(-0.16, 0.11), xycoords='axes fraction', 
                ha='center', va='center',rotation=90,
                arrowprops=dict(arrowstyle='-[, widthB=5.5, lengthB=0.5', lw=1))

    ax1.annotate('Sector', xy=(0.27, -0.15), xytext=(0.27, -0.18), xycoords='axes fraction', 
                ha='center', va='center',rotation=0,
                arrowprops=dict(arrowstyle='-[, widthB=14, lengthB=0.5', lw=1))
    ax1.annotate('Technology', xy=(0.63, -0.15), xytext=(0.63, -0.18), xycoords='axes fraction', 
                ha='center', va='center',rotation=0,
                arrowprops=dict(arrowstyle='-[, widthB=4.2, lengthB=0.5', lw=1))
    ax1.annotate('Policy', xy=(0.81, -0.15), xytext=(0.81, -0.18), xycoords='axes fraction', 
                ha='center', va='center',rotation=0,
                arrowprops=dict(arrowstyle='-[, widthB=3.5, lengthB=0.5', lw=1))
    ax1.annotate('Incident', xy=(0.95, -0.15), xytext=(0.95, -0.18), xycoords='axes fraction', 
                ha='center', va='center',rotation=0,
                arrowprops=dict(arrowstyle='-[, widthB=2.5, lengthB=0.5', lw=1))

    plt.savefig(r'Figs/Figure_3_c.png', dpi=300)
    
    fig = plt.figure(figsize=[2, 8])
    ax2 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    ax2.set_xticks([], [])
    ax2.set_yticks([], [])
    ax2.set_xlim(0, 3000)
    ax2.set_ylim(-0.5, 25.5)
    ax2.spines['right'].set_visible(False)
    ax2.spines['top'].set_visible(False)
    ax2.spines['bottom'].set_visible(False)
    data = []
    for j in range(len(Ls1)):
        for item in impacts[j]:
            data.append(len(df.loc[df[Qs_i[j]].str.contains(item), Qs_i[j]]))
    ax2.barh(np.arange(26), data, height=0.8, color='#D8CB3C')
    for i in range(26):
        ax2.text(data[i], i, str(data[i]), ha='left', va='center', color='black')
    plt.savefig(r'Figs/Figure_3_d.png', dpi=300)
    
    fig = plt.figure(figsize=[8, 2])
    ax3 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    ax3.set_xticks([], [])
    ax3.set_yticks([], [])
    ax3.spines['right'].set_visible(False)
    ax3.spines['top'].set_visible(False)
    ax3.spines['left'].set_visible(False)
    ax3.set_xlim(-0.5, 25.5)
    data = []
    for j in range(len(Ls2)):
        df[Qs_o[j]].fillna('', inplace=True)
        for item in objects[j]:
            data.append(len(df.loc[df[Qs_o[j]].str.contains(item), Qs_o[j]]))
    ax3.bar(np.arange(26), data, width=0.8, color='#D8CB3C')
    for i in range(26):
        ax3.text(i, data[i], str(data[i]), ha='center', va='bottom', color='black')
    plt.savefig(r'Figs/Figure_3_e.png', dpi=300)
