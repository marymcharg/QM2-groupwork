import requests, bs4, pandas as pd
import csv

def getsingles(url):
    allsingles = []
    print("Getting Page %s " %url)
    req = requests.get(url)
    req.raise_for_status()

    while url != "https://www.officialcharts.com/charts/uk-top-40-singles-chart/19701227/750140/":
        soup = bs4.BeautifulSoup(req.text,"lxml")

        # Retrieve chart dates and tidy the format
        sdate = soup.find_all("p", class_="article-date")
        date = sdate[0].text.split("-")[0]

        # Retrieve the artist and single names
        artists = soup.find_all("div", class_="artist")
        singles = soup.find_all("div", class_="title")

        # Create a list of each single, append to master list
        positions = soup.find_all("span", class_="position")
        for i in range (len(positions)): 
            single = [] 
            single.append(date.strip("\r").strip("\n").strip(" "))
            single.append(artists[i].text.strip("\n").strip("\r"))
            single.append(singles[i].text.strip("\n").strip("\r"))
            allsingles.append(single)

        # Find prev week's info, create link
        prevlink = soup.find("a",class_="prev chart-date-directions")
        link = (prevlink["href"])
        link = "http://www.officialcharts.com" + link

        # Write weekly albums to CSV
        with open("official_charts_data.csv","a",newline="", encoding="utf-8") as resultFile:
            wr = csv.writer(resultFile)
            wr.writerows(allsingles)
            resultFile.close()

        # Clear weekly list, proceed to next week's file
        allsingles = []
        getsingles(link)
    else:
        return

def main():
	# Start getting singles from the week ending 2011
    getsingles("https://www.officialcharts.com/charts/uk-top-40-singles-chart/20111225/750140/")

if __name__ == '__main__':
    main()
