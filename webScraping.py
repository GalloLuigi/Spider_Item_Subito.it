import bs4
import requests
import webbrowser
from pprint import pprint

regions = [
    "abruzzo",
    "basilicata",
    "calabria",
    "campania",
    "emilia-romagna",
    "friuli-venezia-giulia",
    "lazio",
    "liguria",
    "lombardia",
    "marche",
    "molise",
    "piemonte",
    "puglia",
    "sardegna",
    "sicilia",
    "toscana",
    "trentino-alto-adige",
    "umbria",
    "valle-d-aosta",
]

int_region = input()
int_region = int(int_region)
LINK = "https://www.subito.it/annunci-"+regions[int_region]+"/vendita/auto/subaru/impreza/?q=subaru+impreza"
print("The link are "+LINK)
PRE_LINK_AD = "https://www.subito.it/auto/"

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

f = open('result.txt', 'a')
old_link_ads = [riga.rstrip('\n') for riga in open('result.txt')]

new_link_ads = []
for link_ad in link_ads:
    if link_ad not in old_link_ads:
        new_link_ads.append(link_ads)
        f.write('%s\n' % link_ad)
f.close()

if new_link_ads:
    print('There are new results . . .')
    for new_link in new_link_ads:
        webbrowser.open(str(new_link))
else:
    print("No new announcements.")

input('\n Program finished.')
