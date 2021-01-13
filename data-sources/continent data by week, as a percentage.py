# line graph for each continent's percentage of charting artists
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def normalise(week):
    total = week["Continent"].value_counts(normalize=True, sort=False) * 100
    dictionary = pd.Series(total).to_dict()
    return dictionary
    

# Make a data frame
df = pd.read_csv("continents.csv", usecols=["Date Charted", "Continent"])
df["Date"] = ""


# Format year
for index in df.index:
    df["Date"] = df["Date Charted"].to_datetime(dayfirst=True, format="%d-%b-%y", unit='y')


# Split dataframe by week
areas = ["North America", "United Kingdom", "Europe", "Oceania", "Asia", "Africa", "South America"]
weeks = df["Date Charted"].unique().tolist()
grouped = df.groupby(df["Date Charted"])
frame = pd.DataFrame(areas, columns=["Areas"])
for w in weeks:
    week = grouped.get_group(w)
    frame[w] = frame.Areas.map(normalise(week))
frame = frame.set_index("Areas")
frame = frame.T
frame.fillna(0, inplace=True)
print(frame.head)
frame.to_csv("country by week.csv")
print("Saved!")

print("Done!")
