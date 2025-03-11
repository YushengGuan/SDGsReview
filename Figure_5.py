import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import Rectangle

plt.rcParams['font.family'] = ['Arial']


names = ['R1', 'V3', '32B', '14B', '7B']


fig, ax = plt.subplots(figsize = (10,2), facecolor = 'none')
plt.subplots_adjust(left=0.1, bottom=0.2, right=0.95, top=0.95)

data_all = []

for n, name in enumerate(names):
    df = pd.read_excel(f'Test/full_text_{name}.xlsx')
    data = df['Time'].values[df['Time'].values >=2]
    data_all.append(data)
    plt.scatter(data, [n+1.2]*len(data), marker='o', s=10, color='steelblue', alpha=0.5, edgecolors='black')
plt.boxplot(data_all, vert=False, widths=0.2, showfliers=False)
plt.xlabel('Time (s)')
plt.yticks(range(1, 6), names)
plt.xlim(0, 400)
plt.ylim(0.5, 6)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.savefig(r'Figs/Figure_5_a.png', dpi=300, transparent=True)


fig, ax = plt.subplots(figsize = (10,2))
plt.subplots_adjust(left=0.1, bottom=0.2, right=0.95, top=0.95)
vp = ax.violinplot(data_all, vert=False, showmeans=False, showmedians=False, showextrema=False)
for i, b in enumerate(vp['bodies']):
    b.set_facecolor('steelblue')
    b.set_edgecolor('black')
    b.set_alpha(1)
ax.add_patch(Rectangle((0, 0.5), 400, 0.5, color='white'))
ax.add_patch(Rectangle((0, 1.5), 400, 0.5, color='white'))
ax.add_patch(Rectangle((0, 2.5), 400, 0.5, color='white'))
ax.add_patch(Rectangle((0, 3.5), 400, 0.5, color='white'))
ax.add_patch(Rectangle((0, 4.5), 400, 0.5, color='white'))
plt.yticks([], [])
plt.xticks([], [])
plt.xlim(0, 400)
plt.ylim(0.5, 6)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
# ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
plt.savefig(r'Figs/Figure_5_b.png', dpi=300)
