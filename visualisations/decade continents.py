# libraries and data
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# Bar graph code
def bar_graph(df, decade):
    # Initialize the figure
    plt.style.use('seaborn-darkgrid')

    # create a color palette
    palette = plt.get_cmap('Dark2')

    # find totals of each continent, normalised
    total = df["Continent"].value_counts(normalize=True).to_frame("Percentage")
    heights = total["Percentage"].tolist()
    height = [i * 100 for i in heights]
    bars = list(total.index)
    y_pos = np.arange(len(bars))

    # Create bars
    colours = ["xkcd:windows blue", "xkcd:amber", "xkcd:greyish", "xkcd:faded green", "xkcd:dusty purple", "xkcd:pale red", "xkcd:medium green"]
    plt.bar(y_pos, height, color=colours)
     
    # Add title and axis names
    if int(decade[0]) == 91:
        plt.title('Area of Origin of UK Top 40 \ncharting artists between 19' + str(decade[0]) + '-2001')    
    elif int(decade[0]) > 11:
        plt.title('Area of Origin of UK Top 40 \ncharting artists between 19' + str(decade[0]) + '-19' + str(int(decade[0]) + 10))
    else:
        plt.title('Area of Origin of UK Top 40 \ncharting artists between 20' + str(decade[0]) + '-20' + str(int(decade[0]) + 10))
    plt.xlabel('Areas')
    plt.ylabel('Percentage of Artists')
     
    # Limits for the Y axis
    plt.ylim(0,100)
     
    # Create names
    plt.xticks(y_pos, bars)
     
    # Save graphic
    plt.show()


# Make a data frame
df = pd.read_csv("continents.csv", usecols=["Date Charted", "Continent"])
df["Year"] = ""


# New column for year charted
for index in df.index:
    df["Year"][index] = str(df["Date Charted"][index])[-2:]
print(df["Year"])


# Split dataframe by decade, starting at '71
year = 11
while year != 71:
    if year < 0:
        year = 91

    decade = []
    if year != 1:
        for x in range(year - 10, year):
            decade.append(str(x).zfill(2))
    else:
        decade = ["91", "92", "93", "94", "95", "96", "97", "98", "99", "00"]

    subsec = df[df["Year"].isin(decade)]
    bar_graph(subsec, decade)
    year = year - 10
else:
    print("Done!")
    
