import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
import matplotlib as mpl



def split_name(names):
    splits = [', ', '， ', ',', '，', ';', '；', '、', ' ']
    for s in splits:
        if s in str(names):
           return names.split(s)
    return [names]


if __name__ == '__main__':
    df = pd.read_excel('Included/影响评估_included_zh.xlsx')
    df_draw = pd.read_excel('worldmap_gaode/country.xlsx')
    for i in df.index:
        name_split = split_name(df.loc[i, 'Q20'])
        for item in name_split:
            df_draw.loc[df_draw['中文名'] == item, 'Count'] += 1/len(name_split)
    df_draw.to_excel('DataDraw/Authorship.xlsx')

    world = gpd.read_file(r'./worldmap_gaode').rename(columns={'NAME_ENG': 'NAME'})
    world_grid = world.merge(df_draw, on='SOC', how='left')
    world_grid['Count'].replace(0, np.nan, inplace=True)

    fig = plt.figure(figsize=(30, 15))
    axes = fig.add_axes([0, 0.025, 0.9, 0.95])

    beutblue = mpl.colors.LinearSegmentedColormap.from_list('beutblue', 
                                             [(0,    '#F5D8D4'),
                                                     (1,    '#BD4B4B')], N=256)
    bins = [0, 1, 3, 10, 30, 100, 500]
    world_grid.plot(column='Count',
                    ax=axes,
                    legend=True,
                    cmap=beutblue,
                    scheme='UserDefined',
                    classification_kwds={'bins': bins[1:]},
                    edgecolor="grey",
                    legend_kwds={'bbox_to_anchor':(0.2, 0.4),
                             'fontsize': 20,
                             'title':'Number of articles',
                             'title_fontsize':'x-large',
                             'labels':[
                                        '(0, 1]',
                                        '(1, 3]',
                                        '(3, 10]',
                                        '(10, 30]',
                                        '(30, 100]',
                                        '(100, 500]',
                                    ],
                             'frameon': True,
                             },
                    missing_kwds={"color": "lightgrey",
                                  "label": "No Data",},
                    )
    axes.axis('off')

    ax1 = fig.add_axes([0.08, 0.5, 0.08, 0.16])
    values = [0] * 11  # 2015-2025
    for i in df.index:
        name_split = split_name(df.loc[i, 'Q20'])
        if '美国' in name_split:
            year = df.loc[i, 'Publication Year']
            if year > 2025 or year < 2015:
                print('未计入', year)
            else:
                values[year-2015] += 1
    ax1.bar(range(11), values, width=0.8, align='center', color='#7255B3')
    ax1.set_xticks(range(11), [str(t) for t in range(2015, 2026)], rotation=90)
    ax1.set_title('U.S.', y=0.9)
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Number of articles')
    ax1.set_ylim(0, 80)

    ax2 = fig.add_axes([0.32, 0.6, 0.08, 0.16])
    EU27 = df_draw.loc[df_draw['EU']==1]['中文名'].values
    values = [0] * 11  # 2015-2025
    for i in df.index:
        name_split = split_name(df.loc[i, 'Q20'])
        flg = 0
        for name in name_split:
            if name in EU27:
                flg = 1
                break
        if flg == 1:
            year = df.loc[i, 'Publication Year']
            if year > 2025 or year < 2015:
                print('未计入', year)
            else:
                values[year-2015] += 1
    ax2.bar(range(11), values, width=0.8, align='center', color='#2C66DC')
    ax2.set_xticks(range(11), [str(t) for t in range(2015, 2026)], rotation=90)
    ax2.set_title('EU27', y=0.9)
    ax2.set_xlabel('Year')
    ax2.set_ylabel('Number of articles')
    ax2.set_ylim(0, 250)

    ax3 = fig.add_axes([0.8, 0.65, 0.08, 0.16]) 
    values = [0] * 11  # 2015-2025
    for i in df.index:
        name_split = split_name(df.loc[i, 'Q20'])
        if '中国' in name_split:
            year = df.loc[i, 'Publication Year']
            if year > 2025 or year < 2015:
                print('未计入', year)
            else:
                values[year-2015] += 1
    ax3.bar(range(11), values, width=0.8, align='center', color='#6FC147')
    ax3.set_xticks(range(11), [str(t) for t in range(2015, 2026)], rotation=90)
    ax3.set_title('China', y=0.9)
    ax3.set_xlabel('Year')
    ax3.set_ylabel('Number of articles')
    ax3.set_ylim(0, 150)

    ax4 = fig.add_axes([0.8, 0.4, 0.08, 0.16])
    values = [0] * 11  # 2015-2025
    for i in df.index:
        name_split = split_name(df.loc[i, 'Q20'])
        if '日本' in name_split:
            year = df.loc[i, 'Publication Year']
            if year > 2025 or year < 2015:
                print('未计入', year)
            else:
                values[year-2015] += 1
    ax4.bar(range(11), values, width=0.8, align='center', color='#4BAEBD')
    ax4.set_xticks(range(11), [str(t) for t in range(2015, 2026)], rotation=90)
    ax4.set_title('Japan', y=0.9)
    ax4.set_xlabel('Year')
    ax4.set_ylabel('Number of articles')
    ax4.set_ylim(0, 35)

    ax5 = fig.add_axes([0.7, 0.15, 0.08, 0.16]) 
    values = [0] * 11  # 2015-2025
    for i in df.index:
        name_split = split_name(df.loc[i, 'Q20'])
        if '澳大利亚' in name_split:
            year = df.loc[i, 'Publication Year']
            if year > 2025 or year < 2015:
                print('未计入', year)
            else:
                values[year-2015] += 1
    ax5.bar(range(11), values, width=0.8, align='center', color='#7ED2F1')
    ax5.set_xticks(range(11), [str(t) for t in range(2015, 2026)], rotation=90)
    ax5.set_title('Australia', y=0.9)
    ax5.set_xlabel('Year')
    ax5.set_ylabel('Number of articles')
    ax5.set_ylim(0, 50)

    ax6 = fig.add_axes([0.6, 0.30, 0.08, 0.16]) 
    values = [0] * 11  # 2015-2025
    for i in df.index:
        name_split = split_name(df.loc[i, 'Q20'])
        if '印度' in name_split:
            year = df.loc[i, 'Publication Year']
            if year > 2025 or year < 2015:
                print('未计入', year)
            else:
                values[year-2015] += 1
    ax6.bar(range(11), values, width=0.8, align='center', color='#AB7E5D')
    ax6.set_xticks(range(11), [str(t) for t in range(2015, 2026)], rotation=90)
    ax6.set_title('India', y=0.9)
    ax6.set_xlabel('Year')
    ax6.set_ylabel('Number of articles')
    ax6.set_ylim(0, 80)

    plt.savefig(r'Figs/Figure_1.png', dpi=600)

    # plt.figure(figsize=(4, 4))
    # plt.subplots_adjust(left=0.2, right=0.95, bottom=0.2, top=0.95)
    # values = [0] * 11  # 2015-2025
    # for i in df.index:
    #     name_split = split_name(df.loc[i, 'Q20'])
    #     if '中国' in name_split:
    #         year = df.loc[i, 'Publication Year']
    #         if year > 2025 or year < 2015:
    #             print('未计入', year)
    #         else:
    #             values[year-2015] += 1
    # plt.bar(range(11), values, width=0.8, align='center', color='#6FC147')
    # plt.xticks(range(11), [str(t) for t in range(2015, 2026)], rotation=90)
    # plt.title('China', y=0.9)
    # plt.xlabel('Year')
    # plt.ylabel('Number of articles')
    # plt.ylim(0, 150)
    # plt.savefig(r'Figs/Figure_1_China.png', dpi=150)
    # 
    # plt.figure(figsize=(4, 4))
    # plt.subplots_adjust(left=0.2, right=0.95, bottom=0.2, top=0.95)
    # values = [0] * 11  # 2015-2025
    # for i in df.index:
    #     name_split = split_name(df.loc[i, 'Q20'])
    #     if '日本' in name_split:
    #         year = df.loc[i, 'Publication Year']
    #         if year > 2025 or year < 2015:
    #             print('未计入', year)
    #         else:
    #             values[year-2015] += 1
    # plt.bar(range(11), values, width=0.8, align='center', color='#4BAEBD')
    # plt.xticks(range(11), [str(t) for t in range(2015, 2026)], rotation=90)
    # plt.title('Japan', y=0.9)
    # plt.xlabel('Year')
    # plt.ylabel('Number of articles')
    # plt.ylim(0, 35)
    # plt.savefig(r'Figs/Figure_1_Japan.png', dpi=150)
    # 
    # plt.figure(figsize=(4, 4))
    # plt.subplots_adjust(left=0.2, right=0.95, bottom=0.2, top=0.95)
    # values = [0] * 11  # 2015-2025
    # for i in df.index:
    #     name_split = split_name(df.loc[i, 'Q20'])
    #     if '美国' in name_split:
    #         year = df.loc[i, 'Publication Year']
    #         if year > 2025 or year < 2015:
    #             print('未计入', year)
    #         else:
    #             values[year-2015] += 1
    # plt.bar(range(11), values, width=0.8, align='center', color='#7255B3')
    # plt.xticks(range(11), [str(t) for t in range(2015, 2026)], rotation=90)
    # plt.title('U.S.', y=0.9)
    # plt.xlabel('Year')
    # plt.ylabel('Number of articles')
    # plt.ylim(0, 80)
    # plt.savefig(r'Figs/Figure_1_US.png', dpi=150)
    # 
    # plt.figure(figsize=(4, 4))
    # plt.subplots_adjust(left=0.2, right=0.95, bottom=0.2, top=0.95)
    # values = [0] * 11  # 2015-2025
    # for i in df.index:
    #     name_split = split_name(df.loc[i, 'Q20'])
    #     if '印度' in name_split:
    #         year = df.loc[i, 'Publication Year']
    #         if year > 2025 or year < 2015:
    #             print('未计入', year)
    #         else:
    #             values[year-2015] += 1
    # plt.bar(range(11), values, width=0.8, align='center', color='#AB7E5D')
    # plt.xticks(range(11), [str(t) for t in range(2015, 2026)], rotation=90)
    # plt.title('India', y=0.9)
    # plt.xlabel('Year')
    # plt.ylabel('Number of articles')
    # plt.ylim(0, 80)
    # plt.savefig(r'Figs/Figure_1_India.png', dpi=150)
    # 
    # EU27 = df_draw.loc[df_draw['EU']==1]['中文名'].values
    # plt.figure(figsize=(4, 4))
    # plt.subplots_adjust(left=0.2, right=0.95, bottom=0.2, top=0.95)
    # values = [0] * 11  # 2015-2025
    # for i in df.index:
    #     name_split = split_name(df.loc[i, 'Q20'])
    #     flg = 0
    #     for name in name_split:
    #         if name in EU27:
    #             flg = 1
    #             break
    #     if flg == 1:
    #         year = df.loc[i, 'Publication Year']
    #         if year > 2025 or year < 2015:
    #             print('未计入', year)
    #         else:
    #             values[year-2015] += 1
    # plt.bar(range(11), values, width=0.8, align='center', color='#2C66DC')
    # plt.xticks(range(11), [str(t) for t in range(2015, 2026)], rotation=90)
    # plt.title('EU27', y=0.9)
    # plt.xlabel('Year')
    # plt.ylabel('Number of articles')
    # plt.ylim(0, 250)
    # plt.savefig(r'Figs/Figure_1_EU27.png', dpi=150)
    # 
    # plt.figure(figsize=(4, 4))
    # plt.subplots_adjust(left=0.2, right=0.95, bottom=0.2, top=0.95)
    # values = [0] * 11  # 2015-2025
    # for i in df.index:
    #     name_split = split_name(df.loc[i, 'Q20'])
    #     if '澳大利亚' in name_split:
    #         year = df.loc[i, 'Publication Year']
    #         if year > 2025 or year < 2015:
    #             print('未计入', year)
    #         else:
    #             values[year-2015] += 1
    # plt.bar(range(11), values, width=0.8, align='center', color='#7ED2F1')
    # plt.xticks(range(11), [str(t) for t in range(2015, 2026)], rotation=90)
    # plt.title('Australia', y=0.9)
    # plt.xlabel('Year')
    # plt.ylabel('Number of articles')
    # plt.ylim(0, 50)
    # plt.savefig(r'Figs/Figure_1_Australia.png', dpi=150)
