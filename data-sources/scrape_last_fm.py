import requests, bs4, pandas as pd
import csv

# adds birthplace and gender of artists to official_charts_data.csv 
# using beautiful soup and www.last.fm, saves complete file as 1971_2011_top_40.csv

def clean_name(name):
    if " FT " in name:
        name = name[:name.find(" FT ")]
    if " FEATURING " in name:
        name = name[:name.find(" FEATURING ")]
    if "/" in name:
        name = name[:name.find("/")]
    if " VS " in name:
        name = name[:name.find(" VS ")]
    return name


def find_artist(dataset):
    """Find artist name in dataset.
    """
    data = pd.read_csv(dataset)
    names = data["Artist Name"]
    found_artists = {}
    found_genders = {}
    birthplaces = []
    gender = []
    for artist in names:
        name = clean_name(artist)
        if name not in found_artists:            
            print("Getting " + name)
            url = name.replace(" ", "+")
            found_artists[name] = find_birthplace(url, found_artists, gender, found_genders)  
            birthplaces.append(found_artists.get(name))
        else:
            birthplaces.append(found_artists.get(name))
            full_url = "https://www.last.fm/music/" + url
            find_gender(full_url, found_genders, gender, name)
    add_to_csv(birthplaces, gender)


def find_birthplace(name, found_artists, gender, found_genders):
    """Scrape LastFM for artist's birthplace.
    
    Args:
        name (str): artist name, spaces replaced with '+'
    
    Returns:
        birthplace (str): birthplace/founding place of artist
    """
    url = "https://www.last.fm/music/" + name

    try:
        req = requests.get(url)
        req.raise_for_status()
        soup = bs4.BeautifulSoup(req.text,"lxml")
        error = soup.find_all("div", class_= "col-sm-3 col-sm-pull-6 error-page-marvin")   
        if error == []:    
            try: 
                data = soup.find_all("dd", class_="catalogue-metadata-description")
                birthplace = data[1].string
                find_gender(url, found_genders, gender, name)
                return birthplace                
            except:
                find_gender(url, found_genders, gender, name)
                return "N/A"
        else:
            try:
                alt_search(name, found_artists, gender, found_genders)
            except:
                gender.append("N/A")
                return "N/A"
    except:
        gender.append("N/A")
        return "N/A"


def alt_search(name, found_artists, gender, found_genders):
    new_name = name[:name.find(" & ")]
    if new_name not in found_artists:
        try:
            url = "https://www.last.fm/music/" + new_name
            req = requests.get(url)
            req.raise_for_status()
            soup = bs4.BeautifulSoup(req.text,"lxml")
            error = soup.find_all("div", class_= "col-sm-3 col-sm-pull-6 error-page-marvin")   
            if error == []:   
                try:
                    data = soup.find_all("dd", class_="catalogue-metadata-description")
                    birthplace = data[1].string
                    found_artists[new_name] = found_artists.pop(name)
                    print("Replacing " + name + " with " + new_name)
                    find_gender(url, found_genders, gender, name)
                    return birthplace
                except:
                    find_gender(url, found_genders, gender, name)
                    return "N/A"
            else:
                gender.append("N/A")
                return "N/A"
        except:
            gender.append("N/A")
                return "N/A"
    else:
        find_gender(url, found_genders, gender, name)
        return found_artists.get(new_name)


def find_gender(url, found_genders, gender, name):
    if name not in found_genders:
        try:
            url = url + "/+tags"
            req = requests.get(url)
            req.raise_for_status()
            soup = bs4.BeautifulSoup(req.text,"lxml")
            error = soup.find_all("div", class_= "col-sm-3 col-sm-pull-6 error-page-marvin")
            if error == []:   
                data = soup.find_all("a", class_="link-block-target")
                count = 0
                num_tags = len(data)
                for tag in data:
                    if "female vocalists" in tag.string:
                        gender.append("F")
                        found_genders[name] = "F"
                        break
                    elif "male vocalists" in tag.string:
                        gender.append("M")
                        found_genders[name] = "M"
                        break
                    count += 1
                    if count == num_tags:
                        gender.append("N/A")
                        found_genders[name] = "N/A"
                    else:
                        continue
            else:
                gender.append("N/A")
                found_genders[name] = "N/A"
        except:
            gender.append("N/A")
            found_genders[name] = "N/A"
    else:
        gender.append(found_genders.get(name))


def add_to_csv(birthplaces, gender):
    """
    Args:
        birthplaces (dict): keys are artist names, values are birthplaces.
    """
    dataset = pd.read_csv("official_charts_data_2.csv")
    dataset.insert(3, "Birthplace", birthplaces)
    dataset.insert(4, "Gender", gender)
    dataset.to_csv("1971_2011_top_40.csv", index=False, encoding="utf-8")
    print("Done!")


def main():
    dataset = "official_charts_data_2.csv"
    find_artist(dataset)


if __name__ == '__main__':
    main()
