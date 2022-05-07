from bs4 import BeautifulSoup
import requests
import json

def get_english():
    html_doc = requests.get('https://en.wikipedia.org/wiki/List_of_towns_in_England').text

    soup = BeautifulSoup(html_doc, 'html.parser')
    tables = soup.findAll("table", {"class": "wikitable"})
    names = []
    for table in tables:
        links = table.findAll("a")
        for link in links:
            if link.text == "1":
                continue
            names.append(link.text)
    
    return names


def get_scottish():
    html_doc = requests.get('https://en.wikipedia.org/wiki/List_of_burghs_in_Scotland').text

    soup = BeautifulSoup(html_doc, 'html.parser')
    tables = soup.findAll("table", {"class": "wikitable"})
    names = []
    for table in tables:
        first_column = table.find("td")
        links = first_column.findAll("a")
        for link in links:
            if link.text == "1":
                continue
            names.append(link.text)
    
    return names

names = get_english() + get_scottish()

with open('noms.json', 'w+') as file:
    d = json.dumps(names)
    print(d)
    file.write(d)