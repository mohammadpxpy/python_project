import requests


city = input("enter name city: ")
url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
data = requests.get(url).json()

     
latitude = data['results'][0]['latitude']
longitude = data['results'][0]['longitude']
name_city = data['results'][0]['name']

url_weather = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
data_weather = requests.get(url_weather).json()

temperature = data_weather['current_weather']['temperature']
windspeed = data_weather['current_weather']['windspeed']
weathercode = data_weather['current_weather']['weathercode']
time = data_weather['current_weather']['time']

print(f"""
      name : {name_city}
      temperature : {temperature}
      windspeed : {windspeed}
      weathercode : {weathercode}
      time : {time}
      """)       
    