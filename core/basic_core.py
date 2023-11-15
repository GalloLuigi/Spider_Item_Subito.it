import bs4
import requests
import webbrowser
from pprint import pprint

import utility.constants
#import tkinter_interface
from utility.constants import RESULT_PATH, PRE_LINK_AD


def make_link(region, brand, model, fuel="benzina"):
    prelink = "https://www.subito.it/annunci-" + region + "/vendita/auto/" + brand + "/" + model

    postlink = "/?q=" + brand + "+" + model
    if fuel == 0:
        return prelink+postlink
    else:
        return prelink+"/"+fuel+postlink


def save_link(link):
    response = requests.get(link)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        return 1
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

    return 0

def make_list_link():
    with open(RESULT_PATH, "r") as f:
        links = f.readlines()
    return links


def open_link(link_car):
    webbrowser.open(link_car)


def open_links(links):
    for link in links:
        open_link(link)


def make_button_color(button, color):
    button.configure(bg=color)


def change_color(button, option):
    if option == 0:
        make_button_color(button, "GREEN")
        return 0
    else:
        make_button_color(button, "RED")
        return 1


def convert_fuel(fuel):
    if fuel == 0:
        return "benzina"
    else:
        return "diesel"

def find_cars(region, brand, model, fuel):
    print("Enter find cars")
    print("Region:"+region)
    print("Brand:"+brand)
    print("Model:"+model)
    fuel=convert_fuel(fuel)
    print("Fuel:"+str(fuel))
    link = make_link(region, brand, model, fuel)
    print("Link:"+link)
    if save_link(link) == 0:
        links = make_list_link()
        open_links(links)
        return 0
    else:
        return 1


def clear_file(file_path):
    open(file_path, 'w').close()

    f = open(file_path, 'r+')
    f.truncate(0)  # need '0' when using r+

