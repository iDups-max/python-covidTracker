import unicornhat as uh
uh.set_layout(uh.PHAT) #uses small layout
uh.brightness(0.3)

uh.set_pixel(0, 0, 255, 0, 0)
uh.set_pixel(0, 1, 0, 255, 0)
uh.set_pixel(2, 0, 0, 0, 255)
uh.show()

import requests


# url = "https://covidapi.info/api/v1/global"

response = requests.get('https://covidapi.info/api/v1/global')
print(response)






print("running main.py")
input() #makes script consistent
