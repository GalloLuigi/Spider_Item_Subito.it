from basic_core import *


def find_cars(region, brand, model):
    link = make_link(region, brand, model)
    save_link(link)
    links = make_list_link()
    open_links(links)
