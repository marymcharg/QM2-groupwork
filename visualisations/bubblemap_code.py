from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import math
import cartopy.crs as ccrs
import pandas as pd
import os
import time

binColours = ['#ea9e08', '#fe7628','#ff464b','#fb0072','#dd009b','#a21ec1','#0642db']
binNumbers = [10, 50, 100, 500, 1000, 10000]
handles = []
#legend
for i in range(len(binColours)):
    if i == 0:
        patch = mpatches.Patch(color=binColours[i], label=f"1 - {binNumbers[i]}")
    elif i == len(binColours) - 1 :
        patch = mpatches.Patch(color=binColours[i], label=f"> {binNumbers[-1]}")
    else:
        patch = mpatches.Patch(color=binColours[i], label=f"{binNumbers[i - 1] + 1} - {binNumbers[i]}")
    handles.append(patch)

#function to plot each individual graph

def make_country_total_map(date, data, ax=None, resolution='map'):

    all_country_total = data[data['Date Charted'] <= date]
    scatters = []
    for _, country_data in all_country_total.groupby('Country of Origin'):
        country_total = len(country_data.index)

        # lists of latitude and longitude for each country
        latitude = country_data["latitude"].iloc[0]
        longitude = country_data["longitude"].iloc[0]
        size = country_total
        colour = binColours[-1]
        for i in range(len(binNumbers)):
                if size <= binNumbers[i]:
                        colour = binColours[i]
                        break

        scatters.append(ax.scatter(longitude, latitude, s=size,
                color=colour, alpha=0.55,
                transform=ccrs.PlateCarree()))


    fontname = 'DejaVu Sans'
    fontsize = 28
    date_x = -53
    date_y = -50
    date_spacing = 65

    # Date text
    text = ax.text(date_x, date_y,
            f"{date.strftime('%b %d, %Y')}",
            color='#555555',
            fontname=fontname, fontsize=fontsize*1.3,
            transform=ccrs.PlateCarree())
    # Running total of unique countries
    count = ax.text(date_x + date_spacing*1.4, date_y,
            f"{len(all_country_total.groupby(['latitude', 'longitude']).count().index)} countries",
            color='#555555', ha='left',
            fontname=fontname, fontsize=fontsize*1.3,
            transform=ccrs.PlateCarree())

    return ax, scatters, text, count

maptype = "PlateCarree"
os.environ["CARTOPY_USER_BACKGROUNDS"] = "BM"


excluded_countries = ["United Kingdom", "Wales", "Ireland"]

#import csv
df = pd.read_csv('map_data.csv', names=['Country of Origin', 'Date Charted', 'latitude', 'longitude'])
df = df[~df["Country of Origin"].isin(excluded_countries)]
df['Date Charted'] = pd.to_datetime(df['Date Charted'])


start_date = datetime(1971, 1, 3)
end_date = datetime(2011, 12, 25)

plt.axis('off')
fig = plt.figure(figsize=(19.8, 10.8))
ax = plt.axes(projection=ccrs.Mercator(min_latitude=-65,
                                       max_latitude=70))

#import custom background, add title etc
ax.background_img(name="BM", resolution='map')
ax.set_extent([-170, 179, -65, 70], crs=ccrs.PlateCarree())
text = ax.text(-120, 67,
            "Total Songs Charting in the UK Top 40 by Country of Origin of the Artist",
            color='#000000',
            fontsize=25,
            fontweight='bold',
            transform=ccrs.PlateCarree())
ax.legend(title="Total Number of Charting Songs", handles=handles, loc=3, prop={'size': 20})
plt.tight_layout(pad=-0.5)
fig.savefig(f"frames/frame_0000.png", dpi=100, facecolor='black')
# generating an image for each week
for ii, days in enumerate(range((end_date - start_date).days // 7 + 1)):
#     date = start_date + (timedelta(days) * 7)
    date = end_date - (timedelta(days) * 7)
    ax, scatters, text, count = make_country_total_map(date, df, ax=ax, resolution='blue')
    fig.tight_layout(pad=-0.5)
    fig.savefig(f"frames/frame_{(ii+1):04d}.png", dpi=100, facecolor='black')
    [s.remove() for s in scatters]
    text.remove()
    count.remove()
