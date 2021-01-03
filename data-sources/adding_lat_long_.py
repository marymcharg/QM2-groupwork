# creates a new csv "map_data.csv" from "1971_2011_top_40_new.csv" with "Country of Origin",
# "Date Charted" and new columns containing latitude and longitude
# removes rows with no data in "Country of Origin" column in "1971_2011_top_40_new.csv"

import pandas as pd

df1 = pd.read_csv("1971_2011_top_40_new.csv")
df2 = pd.read_csv("countries_latitude_and_longitude.csv")
df1["latitude"] = ""
df1["longitude"] = ""

lat_dict = {}
long_dict = {}
for _, row in df2.iterrows():
    lat_dict[row["country"]] = row["latitude"]
    long_dict[row["country"]] = row["longitude"]

df1 = df1[df1["Country of Origin"].isin(lat_dict.keys())]

for index, row in df1.iterrows():
    row["latitude"] = lat_dict[row["Country of Origin"]]
    row["longitude"] = long_dict[row["Country of Origin"]]

print(df1.head())

df1.to_csv("map_data.csv")
