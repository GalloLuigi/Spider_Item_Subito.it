import bs4
import requests
import webbrowser
from pprint import pprint
from utility.constants import RESULT_PATH, PRE_LINK_AD


def make_link(region, brand, model):
    return "https://www.subito.it/annunci-" + region + "/vendita/auto/" + brand + "/" + model \
           + "/?q=" + brand + "+" + model


def save_link(link):
    response = requests.get(link)
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


def make_list_link():
    with open(RESULT_PATH, "r") as f:
        links = f.readlines()
    return links


def open_link(link_car):
    webbrowser.open(link_car)


def open_links(links):
    for link in links:
        open_link(link)


def find_cars(region, brand, model):
    link = make_link(region, brand, model)
    save_link(link)
    links = make_list_link()
    open_links(links)