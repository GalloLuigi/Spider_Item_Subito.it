# Spider_Item_Subito.it
Spider_Item_Subito.it è un progetto Python che consente la ricerca veloce di auto tramite un'interfaccia customTkinter utilizzando la libreria BeautifulSoup per fare web scraping sul sito www.subito.it .

Il progetto è composto da due parti principali:

* Una classe Spider che si occupa di effettuare il web scraping del sito web Subito.it per recuperare i dati delle auto in vendita.
* Un programma Tkinter che fornisce un'interfaccia utente per consentire agli utenti di cercare le auto in base a vari criteri, come marca, modello, prezzo, ecc.
La classe Spider utilizza la libreria BeautifulSoup per analizzare il codice HTML del sito web Subito.it.

**Requisiti:**

- Python 3.6 o successivo
- Libreria beautifulSoup4 4.12.2
- Libreria customtkinter 5.2.1

**Istruzioni di installazione:**

Per installare il progetto, è necessario clonare il repository GitHub:

```
git clone https://github.com/GalloLuigi/Spider_Item_Subito.it
```

Successivamente, è necessario installare le librerie necessarie:

```
pip install beautifulsoup4 
pip install customtkinter
```

**Istruzioni di utilizzo:**

Per utilizzare il progetto, è necessario avviare il programma Tkinter:

```
python custom_tkinter_interface.py
```

**Contributi:**

I contributi al progetto sono ben accetti. Per contribuire al progetto, è necessario creare un fork del repository GitHub e inviare una pull request.

**Esempio di utilizzo:**

![Immagine 2023-11-23 214808](https://github.com/GalloLuigi/Spider_Item_Subito.it/assets/71981111/e793eb90-52ac-40e2-8c87-8db65e905d7c)

Premendo il bottone "Find" il programma prima aprirà nel broswer predefinito tutti gli anninci in Campania di auto a benzina con marca "subaru" e nome "impreza".

NB: E' possibile tramite il sottomenu "Max Tabs" modificare il numero massimo di schede da aprire (default 20).


**Note:**

- Il progetto è ancora in fase di sviluppo.
- Il progetto è stato testato solo su sistemi operativi Windows.

