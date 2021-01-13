# fix scottish census formatting
import pandas as pd

df = pd.read_csv("2011 scotland.csv", usecols=["All people", "5295403"])
df = df.T
df.to_csv("2011 scotland.csv", index=False, header=False)

df = pd.read_csv("2001 scotland.csv", usecols=["All people", "5062011"])
df = df.T
df.to_csv("2001 scotland.csv", index=False, header=False)
