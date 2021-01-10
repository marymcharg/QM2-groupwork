# creates "continents.csv" from "1971_2011_top_40_new.csv" & "Countries-Continents.csv"
# removes rows with no data in "Contry of Origin" column in "1971_2011_top_40_new.csv"

CONTINENT = 0
COUNTRY = 1

import pandas as pd
import numpy as np

df1 = pd.read_csv("1971_2011_top_40_new.csv")
df2 = pd.read_csv("Countries-Continents.csv")


# make dict of country to continent
df2.set_index("Country", inplace=True)
cont_dict = df2.T.to_dict("records")[0]

# set the UK as its own continent (for the sake of comparison to other continents)
cont_dict["United Kingdom"] = "United Kingdom"


# drop rows with no Country of Origin
df1.replace("", np.nan, inplace=True)
df1.dropna(subset=["Country of Origin"], inplace=True)


# insert continents
for row in df1:
    df1["Continent"] = df1["Country of Origin"].map(cont_dict)

print(df1.head())
df1.to_csv("continents.csv")
