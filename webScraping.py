# Python Import
import bs4
import requests
import webbrowser
from pprint import pprint

# Project Import
from utility.constants import RESULT_PATH, PRE_LINK_AD
from data.regions import regions
from data.brands import brands


# Definire una funzione per aprire un link nel browser
def open_link(link_car):
    webbrowser.open(link_car)


# Take input region 3
int_region = input()
int_region = int(int_region)

# Take input brand 0
int_brand = input()
int_brand = int(int_brand)

# Take input model impreza
model = input()

LINK = "https://www.subito.it/annunci-" + regions[int_region] + "/vendita/auto/" + brands[int_brand] + "/" + model \
       + "/?q=" + brands[int_brand] + "+" + model

print("The link are "+LINK)


response = requests.get(LINK)
response.raise_for_status()
soup = bs4.BeautifulSoup(response.text, 'html.parser')
div_ads = soup.find('div', class_='ListingContainer_col__1TZpb ListingContainer_items__3lMdo col items')
a_ads = div_ads.find_all('a')
link_ads = []
for a_ad in a_ads:
    link_ad = str(a_ad.get('href'))
    if PRE_LINK_AD in link_ad:
        link_ads.append(link_ad)

pprint(link_ads)

f = open(RESULT_PATH, 'a')
old_link_ads = [riga.rstrip('\n') for riga in open(RESULT_PATH)]

new_link_ads = []
for link_ad in link_ads:
    if link_ad not in old_link_ads:
        new_link_ads.append(link_ads)
        f.write('%s\n' % link_ad)
f.close()

# Leggere la lista di link da un file di testo
with open(RESULT_PATH, "r") as f:
    links = f.readlines()

# Aprire ogni link nel browser
for link in links:
    open_link(link)


input('\n Program finished.')
