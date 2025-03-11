import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import matplotlib as mpl

plt.rcParams['font.family'] = ['Arial']


def split_Q1(names):
    from Figure_1 import split_name
    if names == '1-17':
        return [str(_) for _ in range(1, 18)]
    else:
        return split_name(names)


def split_Q2(names):
    out = []
    if '一' in str(names) or '1' in str(names):
        out.append(1)
    if '二' in str(names) or '2' in str(names):
        out.append(2)
    if '三' in str(names) or '3' in str(names):
        out.append(3)
    return out


if __name__ == '__main__':
    df = pd.read_excel(r'Included/影响评估_included_zh.xlsx')

    fig = plt.figure(figsize=(18, 10))
    beutblue = mpl.colors.LinearSegmentedColormap.from_list('beutblue', 
                                             [(0,    '#ffffff'),
                                                    (1,    '#008F7A')], N=256)
    bins = [0, 1, 4, 16, 64, 256, 1024]

    df_draw = pd.DataFrame([[0]*17 for _ in range(3)])
    for i in df.index:
        Q1 = split_Q1(df.loc[i, 'Q1'])
        Q2 = split_Q2(df.loc[i, 'Q2'])
        try:
            for item1 in Q1:
                for item2 in Q2:
                    df_draw.loc[int(item2)-1, int(item1)-1] += 1
        except Exception as e:
            print(i, e)
    df_draw_log = np.log2(df_draw)

    ax1 = fig.add_axes([0, 0.7, 0.8, 0.15])
    im = ax1.imshow(df_draw_log, cmap=beutblue, origin='lower', vmin=0, vmax=10)
    # cbar = fig.colorbar(im, ax=ax1, label='Number of articles',orientation='horizontal',location='top',fraction=0.02,pad=0.04,anchor=(0.75, 0))
    # cbar.set_ticks(list(range(11)))
    # cbar.set_ticklabels([2**_ for _ in range(11)])
    for i in range(df_draw.shape[0]):
        for j in range(df_draw.shape[1]):
            if df_draw.loc[i, j] != 0:
                text = ax1.text(j, i, df_draw.loc[i, j],
                               ha="center", va="center", color="black", fontsize=10)
    # ax1.set_xticks(np.linspace(0, 16, 17), ['SDG'+str(_) for _ in range(1, 18)])
    ax1.set_xticks([], [])
    ax1.set_yticks(np.linspace(0, 2, 3), ['Level 1', 'Level 2', 'Level 3'])

    ax4 = fig.add_axes([0.15, 0.87, 0.5, 0.1])
    ax4.bar(range(0, 17), df_draw.sum(axis=0), color='#6BBDB1')
    ax4.set_xticks([], [])
    ax4.set_xlim([-1, 17])
    ax4.set_yticks([], [])
    ax4.spines['right'].set_visible(False)
    ax4.spines['top'].set_visible(False)
    ax4.spines['left'].set_visible(False)
    for i in range(17):
        ax4.text(i, df_draw.sum(axis=0)[i], df_draw.sum(axis=0)[i], ha="center", va="bottom", color="black", fontsize=10)

    ax6 = fig.add_axes([0.68, 0.7, 0.1, 0.15])
    level_count = [0] * 3
    for i in df.index:
        Q2 = split_Q2(df.loc[i, 'Q2'])
        for item2 in Q2:
            level_count[item2-1] += 1
    ax6.barh(range(0, 3), level_count, color='#6BBDB1')
    ax6.set_xticks([], [])
    ax6.set_yticks([], [])
    ax6.spines['right'].set_visible(False)
    ax6.spines['top'].set_visible(False)
    ax6.spines['bottom'].set_visible(False)
    for i in range(3):
        ax6.text(level_count[i], i, level_count[i], ha="left", va="center", color="black", fontsize=10)


    courses = ['社会科学', '环境科学', '管理', '经济学', '工程', '生物', '能源', '医药', '跨学科', '其它']
    courses_names = ['Social', 'Environmental', 'Management', 'Economics', 'Engineer', 'Biology', 'Energy', 'Medical', 'Multidisciplinary', 'Others']
    df_draw = pd.DataFrame([[0]*17 for _ in range(len(courses))])
    for i in df.index:
        Q1 = split_Q1(df.loc[i, 'Q1'])
        Q19 = df.loc[i, 'Q19']
        try:
            flg = 0
            for j, c in enumerate(courses[:-1]):
                if c in Q19:
                    flg = 1
                    for item1 in Q1:
                        df_draw.loc[j, int(item1)-1] += 1
            if flg == 0:
                for item1 in Q1:
                    df_draw.loc[9, int(item1)-1] += 1
        except Exception as e:
            print(i, e)
    df_draw_log = np.log2(df_draw+1)
    
    
    ax2 = fig.add_axes([0, 0.1, 0.8, 0.5])
    im = ax2.imshow(df_draw_log, cmap=beutblue, origin='lower', interpolation='nearest', vmin=0, vmax=10)
    # cbar = fig.colorbar(im, ax=ax2, label='Number of articles',orientation='horizontal',location='top',fraction=0.02,pad=0.04,anchor=(0.75, 0))
    # cbar.set_ticks(list(range(11)))
    # cbar.set_ticklabels([2**_ for _ in range(11)])
    for i in range(df_draw.shape[0]):
        for j in range(df_draw.shape[1]):
            if df_draw.loc[i, j] != 0:
                text = ax2.text(j, i, df_draw.loc[i, j],
                               ha="center", va="center", color="black", fontsize=10)
    ax2.set_xticks(np.linspace(0, 16, 17), ['SDG'+str(_) for _ in range(1, 18)])
    ax2.set_yticks(np.linspace(0, 9, 10), courses_names, rotation=0, ha='right')

    course_count = [0] * 10
    for i in df.index:
        Q19 = df.loc[i, 'Q19']
        try:
            flg = 0
            for j, c in enumerate(courses[:-1]):
                if c in Q19:
                    flg = 1
                    course_count[j] += 1
            if flg == 0:
                course_count[-1] += 1
        except Exception as e:
            print(i, e)

    ax5 = fig.add_axes([0.8, 0.1, 0.1, 0.5])
    ax5.barh(range(0, 10), course_count, color='#6BBDB1')
    ax5.set_ylim([-0.5, 9.5])
    ax5.set_yticks([], [])
    ax5.set_xticks([], [])
    ax5.spines['right'].set_visible(False)
    ax5.spines['top'].set_visible(False)
    ax5.spines['bottom'].set_visible(False)
    for i in range(10):
        ax5.text(course_count[i], i, course_count[i], ha="left", va="center", color="black", fontsize=10)
    
    df_draw = pd.DataFrame([[0]*3 for _ in range(len(courses))])
    for i in df.index:
        Q2 = split_Q2(df.loc[i, 'Q2'])
        Q19 = df.loc[i, 'Q19']
        try:
            flg = 0
            for j, c in enumerate(courses[:-1]):
                if c in Q19:
                    flg = 1
                    for item2 in Q2:
                        df_draw.loc[j, int(item2)-1] += 1
            if flg == 0:
                for item1 in Q2:
                    df_draw.loc[9, int(item1)-1] += 1
        except Exception as e:
            print(i, e)
    df_draw_log = np.log2(df_draw+1)

    ax3 = fig.add_axes([0.62, 0.1, 0.2, 0.54])
    im = ax3.imshow(df_draw_log, cmap=beutblue, origin='lower', interpolation='nearest', vmin=0, vmax=10)
    for i in range(df_draw.shape[0]):
        for j in range(df_draw.shape[1]):
            if df_draw.loc[i, j] != 0:
                text = ax3.text(j, i, df_draw.loc[i, j],
                               ha="center", va="center", color="black", fontsize=10)
    ax3.set_xticks(np.linspace(0, 2, 3), ['Level '+str(_) for _ in range(1, 4)])
    ax3.set_yticks([], [], rotation=0, ha='right')
    cbar = fig.colorbar(im, ax=ax3, label='Number of articles',orientation='horizontal',location='top',fraction=0.027,pad=0.04,anchor=(0.7, -20))
    cbar.set_ticks(list(range(11)))
    cbar.set_ticklabels([2**_ for _ in range(11)])
    
    plt.savefig(r'Figs/Figure_2.png', dpi=600)
