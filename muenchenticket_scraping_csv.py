# muenchenticket scraping

import locale
from datetime import datetime

import requests
from bs4 import BeautifulSoup

from urllib.parse import urlparse

import csv

locale.setlocale(locale.LC_ALL, 'de_DE.utf8')

url = "https://www.muenchenticket.de/tickets/spielstaetten/location_l42gnk9n3tf8"
hostname = urlparse(url).hostname

abfrage = requests.get(url)

parsed = BeautifulSoup(abfrage.content, 'html.parser')

events = parsed.find_all('tr', class_="link_to_detail")

liste_header = ['Jahr', 'Monat', 'Tag', 'Uhrzeit_Stunde', 'Uhrzeit_Minute', 'Ort', 'URL' ,'Eventname']
liste_events = list()

anzahl_events = events.__len__()

for x in range(0, anzahl_events):
    eventname = events[x].contents[8].contents[1].contents[1].contents[0]
    eventort = (events[x].contents[8].contents[1].contents[4].contents[0]).strip()
    event_ticketurl = hostname + events[x].contents[2].contents[1]['href']

    datum_monat_jahr = events[x].contents[4].contents[1].contents[2]
    datum_monat_jahr = datum_monat_jahr.strip()

    datum_tag_zahl = events[x].contents[2].contents[1].contents[1].contents[0]

    datum_uhrzeit = events[x].contents[6].contents[1].contents[0]
    datum_uhrzeit = datum_uhrzeit.strip()[0:5]

    datum_kompakt = datetime.strptime(
        (datum_monat_jahr.strip() + " " + datum_tag_zahl.strip() + " - " + datum_uhrzeit.strip()[0:5]),
        '%B %Y %d - %H:%M')

    liste_events.append((datum_kompakt.year,
                         datum_kompakt.month,
                         datum_kompakt.day,
                         datum_kompakt.hour,
                         datum_kompakt.minute,
                         eventort,
                         eventname,
                         event_ticketurl)
                        )

# for x in range(0, anzahl_events):
#   print("Datum: ", liste_events[x]['Jahr'])

print(list(liste_events))

with open('daten', 'w') as f:
    # using csv.writer method from CSV package
    write = csv.writer(f)
    write.writerow(liste_header)
    write.writerows(liste_events)
