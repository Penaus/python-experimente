import math
import numpy
import mvg_api

station_id = mvg_api.get_id_for_station('Sendlnger Tor')
abfahrten_rohdaten = mvg_api.get_departures(station_id)

#abfahrten_gesamt = numpy.array([1,1],[1,1])

tram_18_schwansee = ['TRAM', '18', 'Schwanseestraße']
tram_18_gondrell  = ['TRAM', '18', 'Gondrellplatz']


for x in range(len(abfahrten_rohdaten)):
    if abfahrten_rohdaten[x].get("product") == tram_18_schwansee[0] and abfahrten_rohdaten[x].get("label") == tram_18_schwansee[1] \
            and abfahrten_rohdaten[x].get("destination") == tram_18_schwansee[2] :
        zeit = abfahrten_rohdaten[x].get("departureTimeMinutes")
        if zeit > 60:
            tram_18_schwansee.append(str(math.trunc(zeit/60))+'h '+str(math.trunc(zeit%60))+'m')
        else:
            tram_18_schwansee.append(zeit)

i=0
while i < len(tram_18_schwansee):
    print(tram_18_schwansee[i])
    i +=1
