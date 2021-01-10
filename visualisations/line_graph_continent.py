# libraries and data
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Make a data frame
df = pd.read_csv("continents.csv", index_col="Date Charted", usecols=["Date Charted", "Continent"])

# Initialize the figure
plt.style.use('seaborn-darkgrid')

# create a color palette
palette = plt.get_cmap('Set1')

total = df["Continent"].value_counts().to_frame('Count')
print("\nTotal counts: \n", total)

height = list(total["Count"].tolist())
bars = list(total.index)
y_pos = np.arange(len(bars))

# Create bars and choose color
plt.bar(y_pos, height, color = (0.5,0.1,0.5,0.6))
 
# Add title and axis names
plt.title('Area of Origin of UK Top 40 \ncharting artists between 1971-2011')
plt.xlabel('Areas')
plt.ylabel('Number of Artists')
 
# Limits for the Y axis
plt.ylim(0,50000)
 
# Create names
plt.xticks(y_pos, bars)
 
# Show graphic
plt.show()







