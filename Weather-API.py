import requests
#import os
from datetime import datetime

api_key = '87d845b0b6cf29baa1a73cc34b067a95'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')
file = open("weatherapi.txt","w")
file.write(f'{"Weather Stats for - {}  || {}".format(location.upper(), date_time)}')
file.close()
new_line = "Current temperature is: {:.2f} deg C".format(temp_city)
new_line1 = "Current weather desc  : {}".format(weather_desc)
new_line2 = "Current Humidity      : {} %".format(hmdt)
new_line3 = "Current wind speed    : {} kmph".format(wind_spd)
with open("weatherapi.txt","a") as a_file:
    a_file.write("\n")
    a_file.write(new_line)
    a_file.write("\n")
    a_file.write(new_line1)
    a_file.write("\n")
    a_file.write(new_line2)
    a_file.write("\n")
    a_file.write(new_line3)