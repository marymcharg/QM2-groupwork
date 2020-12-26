import os, csv
import pandas as pd

LAST = -1

def remove_cities(dataset):
    df = pd.read_csv(dataset)
    locations = df["Birthplace"]
    countries = []
    for place in locations:
        place = str(place)
        if place == "nan":
            countries.append("")
        elif "Tanzania, United Republic of" in place:
            countries.append("Tanzania")
        else:
            regions = place.split(",")
            countries.append(regions[LAST].strip())
    df.insert(4, "Country of Origin", countries)
    df.to_csv("1971_2011_top_40_new.csv", index=False)
    

def main():
    dataset = "1971_2011_top_40.csv"
    remove_cities(dataset)
    print("Done!")


if __name__ == '__main__':
    main()
