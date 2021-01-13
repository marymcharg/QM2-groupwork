# make a line graph, featuring each area,
# showing percentage of charting artists from those areas

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('continents percentage by week.csv', index_col=0, parse_dates=True)
areas = list(df)

# Initialize the figure
plt.style.use('seaborn-darkgrid')

# create a color palette
palette = plt.get_cmap('Dark2')

# plotting time
fig = df[areas].plot(marker=".", alpha=0.7, linestyle='None', legend=False)
fig.set_ylabel("Percentage of charting artists")
fig.set_title("Areas of origin of UK Top 40 \ncharting artists between 1971-2011")

# adjust plot size by -20% to fit in legend
box = fig.get_position()
fig.set_position([box.x0, box.y0, box.width * 0.8, box.height])
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.show()
