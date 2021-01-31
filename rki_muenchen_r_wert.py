import requests
from bs4 import BeautifulSoup

abfrage = requests.get(
    "https://www.lgl.bayern.de/gesundheit/infektionsschutz/infektionskrankheiten_a_z/coronavirus/karte_coronavirus/index.htm")
soup = BeautifulSoup(abfrage.text, "lxml")
landkreise = soup.find(id='tableLandkreise')
muc_daten = landkreise.text[(landkreise.text.index("München Stadt")): (landkreise.text.index("Neu-Ulm"))]
muc_klein = muc_daten.splitlines()

anzahl_faelle = muc_klein[2].strip()
anzahl_ggue_vortag = muc_klein[4].strip()
faelle_je_100k = muc_klein[5].strip()
faelle_letzten_7_tage = muc_klein[6].strip()
sieben_tage_inzidenz = muc_klein[7].strip()
todesfaelle_gesamt = muc_klein[9].strip()

anzahl_ggue_vortag = anzahl_ggue_vortag.replace("(", "")
anzahl_ggue_vortag = anzahl_ggue_vortag.replace(")", "")

print("LHM Corona Infos")
print("Fälle gesamt: \t\t\t", anzahl_faelle)
print("Anzahl ggü Vortag: \t\t", anzahl_ggue_vortag)
print("Fälle je 100k: \t\t\t", faelle_je_100k)
print("Fälle letzte Woche: \t", faelle_letzten_7_tage)
print("Inzidenz-Wert: \t\t\t", sieben_tage_inzidenz)
print("Tote gesamt LHM: \t\t", todesfaelle_gesamt)
