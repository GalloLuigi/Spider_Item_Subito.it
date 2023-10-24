import bs4,requests,webbrowser

LINK="https://www.subito.it/annunci-campania/vendita/auto/subaru/impreza/?q=subaru+impreza"
PRE_LINK_ANNUNCIO="https://www.subito.it/auto/"

response = requests.get(LINK)
response.raise_for_status()
soup=bs4.BeautifulSoup(response.text,'html.parser')
div_annunci=soup.find('div',class_='ListingContainer_col__1TZpb ListingContainer_items__3lMdo col items')
a_annunci=div_annunci.find_all('a')
link_annunci = []
for a_annuncio in a_annunci:
    link_annuncio =str(a_annuncio.get('href'))
    if PRE_LINK_ANNUNCIO in link_annuncio:
            link_annunci.append(link_annuncio)

from pprint import pprint
pprint(link_annunci)

f = open('risultati_salvati.txt','a')
old_link_annunci = [riga.rstrip('\n') for riga in open('risultati_salvati.txt')]

new_link_annunci = []
for link_annuncio in link_annunci:
    if link_annuncio not in old_link_annunci:
        new_link_annunci.append(link_annuncio)
        f.write('%s\n' % link_annuncio)
f.close()

if new_link_annunci:
    print('Ci sono nuovi risultati . . .')
    for new_link in new_link_annunci:
        webbrowser.open(new_link)
else:
    print("Nessun nuovo annuncio.")

input('\n Programma terminato')