#WeatherApp Markus Dezelak Bellevue University Intro to Programming
#Featuring OpenWeather API Data and Wttr.In Console Weather Data

import json, requests

#Welcome Message

print("\t\tWelcome to my Weather Forecast App!\n\n")
print("Enter your Zip Code next and get Current Temps and a 3 Day Forecast!\n\n")
base_url = "https://api.openweathermap.org/data/2.5/weather"
appid = "338cc5271d9fc6f08df4e25459c6a953"
city = int(input("Enter Zip Code : \n"))

url = f"{base_url}?q={city}&units=imperial&APPID={appid}"
print(url)
print()

response = requests.get(url)
unformated_data = response.json()

#print(unformated_data)

temp = unformated_data["main"]["temp"]
print(f"The current temp is: {temp}")

temp_max = unformated_data["main"]["temp_max"]
print(f"The max temp is: {temp_max}")

 #Display 3 Day Forecast From Wttr.In
def report(C):
    url = 'https://wttr.in/{}'.format(C)
    try:
        data = requests.get(url)
        T = data.text
    except:
        T = "Error Occurred"
    print(T)
  
report(city)

#program_end
print("Thank you! Have a nice day !")



