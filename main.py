import unicornhat as uh
uh.set_layout(uh.PHAT) #uses small layout
uh.brightness(0.3)

import requests as r
from datetime import datetime

lastDate = r.get('https://covidapi.info/api/v1/latest-date').text
data = r.get('https://covidapi.info/api/v1/country/GBR/latest').json()

confirmed = data['result'][lastDate]['confirmed']
deaths = data['result'][lastDate]['deaths']
recovered = data['result'][lastDate]['recovered']

print ''
print 'UK stats, last updated',lastDate
print ''


print 'confirmed cases: ' , confirmed
print 'confirmed deaths: ' , deaths
print 'confirmed recoveries: ' , recovered
# print str(deaths)[0]

deathsThousands = deaths / 1000

for i in range(deathsThousands):    
    uh.set_pixel(i, 3, 255, 0, 0)

    if deathsThousands > 8:
        for i in range(deathsThousands - 8):    
            uh.set_pixel(i, 2, 255, 0, 0) #line 2

    if deathsThousands > 16:
        for i in range(deathsThousands - 16):    
            uh.set_pixel(i, 1, 255, 0, 0) #line 3


uh.show()

print ''
print 'Press ENTER to exit.'
input() #makes script consistent
