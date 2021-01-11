import pandas as pd

df = pd.read_csv("census_great_britain_gender.csv", index_col = "Date")
df

df["Male percentage"] = df["Male"]/df["Total"]
df["Female percentage"] = df["Female"]/df["Total"]
df

import matplotlib.pyplot as plt

x1 = [1971.0, 1981.0, 1991.0, 2001.0, 2011]
y1 = [0.513944, 0.513542, 0.515841, 0.513896, 0.508878]
plt.title("Percentage of women, census data vs. top artists")
y2 = [0.6562, 0.7285, 0.7328, 0.7217, 0.7217]
plt.ylim(0.2,0.8)
plt.ylabel("Percentage of women")
plt.xlabel("Decades")
plt.plot(x1,y2, label="top charts")
plt.plot(x1,y1, label="census")
plt.legend()
