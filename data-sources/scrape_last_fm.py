import requests, bs4, pandas as pd
import csv


def clean_name(name):
    if " FT " in name:
        name = name[:name.find(" FT ")]
    if "/" in name:
        name = name[:name.find("/")]
    if " VS " in name:
        name = name[:name.find(" VS ")]
    return name


def find_artist(dataset):
    """Find artist name in dataset, .
    """
    data = pd.read_csv(dataset)
    names = data["Artist Name"]
    found_artists = {}
    birthplaces = ["Birthplaces"]
    for artist in names:
        name = clean_name(artist)
        if name not in found_artists:            
            print("Getting " + name)
            url = name.replace(" ", "+")
            found_artists[name] = find_birthplace(url, found_artists)  
            birthplaces.append(found_artists.get(name))          
        else:
            birthplaces.append(found_artists.get(name))
    add_to_csv(birthplaces)


def find_birthplace(name, found_artists):
    """Scrape LastFM for artist's birthplace.
    
    Args:
        name (str): artist name, spaces replaced with '+'
    
    Returns:
        birthplace (str): birthplace/founding place of artist
    """
    url = "https://www.last.fm/music/" + name
    
    req = requests.get(url)
    if req.status_code == 200:
        req.raise_for_status()
        soup = bs4.BeautifulSoup(req.text,"lxml")
        try: 
            data = soup.find_all("div", class_="metadata-column")
            birthplace = data[1]
            return birthplace                
        except:
            return "N/A"
    else:
        try:
            alt_search(name, found_artists)
        except:
            return "ARTIST NOT FOUND"


def alt_search(name, found_artists):
    new_name = name[:name.find(" & ")]
    if new_name not in found_artists: 
        url = "https://www.last.fm/music/" + new_name
        req = requests.get(url)
    if req.status_code == 200:
        req.raise_for_status()
        soup = bs4.BeautifulSoup(req.text,"lxml")
        try:
            data = soup.find_all("div", class_="metadata-column")
            birthplace = data[1]
            return birthplace
            found_artists[new_name] = found_artists.pop(name)
            print("Replacing " + name + " with " + new_name)
        except:
            return IndexError
    else:
        return found_artists.get(new_name)


def add_to_csv(birthplaces):
    """
    Args:
        birthplaces (dict): keys are artist names, values are birthplaces.
    """
    dataset = pd.read_csv("official_charts_data.csv")
    dataset.insert(3, "Birthplace", birthplaces)
    dataset.to_csv("official_charts_birthplaces.csv", index=False, encoding="utf-8")


def main():
    dataset = "official_charts_data.csv"
    find_artist(dataset)


if __name__ == '__main__':
    main()
