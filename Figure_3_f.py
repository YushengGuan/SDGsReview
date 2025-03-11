import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.family'] = ['Arial']

df = pd.read_excel(r'Included/影响评估_included_zh.xlsx')


air = ['PM2.5', 'PM10', 'PM', 'SO2', 'NOx', 'VOC']
climate = ['CO2', 'CH4', 'N2O', '氟', 'GHG']
water = ['TN', 'TP', 'COD', 'BOD', '硝酸盐', '硫酸盐', '磷酸盐', 'NH4', '氰', '农', '肥', '粪', '菌']
metal = ['Fe', 'Cu', 'Cr', 'Cd', 'Mn', 'Ni', 'Co', 'As']
waste = ['塑料', '固体', '医疗', '有害']

air_names = air
climate_names = ['CO2', 'CH4', 'N2O', 'F-related', 'GHG']
water_names = ['TN', 'TP', 'COD', 'BOD', 'NO3', 'SO4', 'PO4', 'NH4', '-CN', 'Pesticide', 'Fertilizer', 'Faeces', 'Infectives']
metal_names = metal
waste_names = ['Plastics', 'Solid', 'Medical', 'Hazardous']

airs = []
for j in range(len(air)):
    if j == 2:
        airs.append(len(df.loc[(df['Q9'].str.contains(air[j]) & ~df['Q9'].str.contains('PM2.5') & ~df['Q9'].str.contains('PM10')), 'Q9']))
    else:
        airs.append(len(df.loc[df['Q9'].str.contains(air[j]), 'Q9']))

climates = [len(df.loc[df['Q9'].str.contains(climate[j]), 'Q9']) for j in range(len(climate))]
waters = [len(df.loc[df['Q9'].str.contains(water[j]), 'Q9']) for j in range(len(water))]
metals = [len(df.loc[df['Q9'].str.contains(metal[j]), 'Q9']) for j in range(len(metal))]
wastes = [len(df.loc[df['Q9'].str.contains(waste[j]), 'Q9']) for j in range(len(waste))]

# 数据准备
df_draw = [airs, climates, waters, metals, wastes]
df_all = [item for sublist in df_draw for item in sublist]
categories = ['Air', 'Climate', 'Water', 'Metals', 'Wastes']
subcategories = [air_names, climate_names, water_names, metal_names, waste_names]  # 假设这些是子类别的列表

# 将子类别合并为一个列表
all_subcategories = [item for sublist in subcategories for item in sublist]

# 环形分组柱状图的参数设置
N = len(all_subcategories)  # 子类别的数量
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]  # 闭合图形

# 绘图
fig, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(polar=True))
width = 2 * np.pi / N+2


# 定义一个额外的角度来表示空白区域的大小
blank_angle = 0.05  # 可以根据需要调整空白区域的大小
angles = np.concatenate(([blank_angle], np.array(angles[1:])+blank_angle))

cat_names = ['Air', 'Climate', 'Water', 'Metals', 'Wastes']
count = 0

# 绘制每个子类别的柱状图
start_angle_idx = 0
for data, subcat in zip(df_draw, subcategories):
    end_angle_idx = start_angle_idx + len(subcat)
    bars = ax.bar(angles[start_angle_idx:end_angle_idx], data, width=0.1, bottom=4)
    # 在每个柱状图上方添加数据标签
    print(data)
    print(subcat)
    print(angles[start_angle_idx:end_angle_idx])
    for i in range(len(data)):
        angle = angles[start_angle_idx:end_angle_idx][i]
        r = 90-angle/np.pi*180 if angle < np.pi else 270-angle/np.pi*180
        ha = 'left' if angle < np.pi else 'right'
        ax.text(angle, data[i]*3, f'{subcat[i]}: {data[i]}', ha=ha, va='center', rotation=r)
    ax.text(np.average(angles[start_angle_idx:end_angle_idx]), 2, cat_names[count], ha='center', va='center')

    count += 1
    start_angle_idx = end_angle_idx



# 设置图表的标签
ax.set_xticks([], [])
ax.set_theta_zero_location('N')
ax.grid(False)
ax.set_theta_direction(-1)
ax.set_theta_zero_location('N')
ax.set_rlabel_position(0)
ax.spines['polar'].set_color('lightgrey')
ax.spines['polar'].set_linewidth(20)
ax.spines['polar'].set_alpha(0.5)

# 设置纵坐标为对数坐标轴
ax.set_yscale('log', base=2)
ax.set_ylim(0.25, 512)
ax.set_yticks([4, 16, 64, 512], [4, 16, 64, 512], ha='right')

# ax.barh([500], [np.pi*2], height=0.5, color='grey', alpha=1)

# 保存图表
plt.savefig(r'Figs/Figure_3_f.png', dpi=300)