import unicornhat as uh
uh.set_layout(uh.PHAT) #uses small layout
uh.brightness(0.3)

uh.set_pixel(0, 0, 255, 0, 0)
uh.set_pixel(0, 1, 0, 255, 0)
uh.set_pixel(2, 0, 0, 0, 255)
uh.show()

import requests as r
import json #needed?
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

print ''
print 'Press ENTER to exit.'
input() #makes script consistent
