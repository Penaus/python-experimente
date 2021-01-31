import json
import time

import requests

stunde = time.localtime().tm_hour
stunde = str(stunde) + ":00:00"

abfrage = requests.get(
    "https://www.mcfit.com/de/auslastung/antwort/request.json?tx_brastudioprofilesmcfitcom_brastudioprofiles%5BstudioId%5D=1879795550")

parsed = json.loads(abfrage.content)

for x in parsed['items']:
    if x['startTime'] == stunde:
        print("gefunden")
        print("prozent", x['percentage'])
        print("auslastung", x['level'])

        break
else:
    print("not there")
