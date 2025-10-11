import requests

while True:
    start = input("<< exit >> \nfor start click << ENTER >>").lower()
    if len(start) == 0 :
        name = input("country name: ").replace(" ","")
        url = f"https://restcountries.com/v3.1/name/{name}"
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            data_government = data[0]['name']['official']
            data_capital = data[0]['capital']
            data_currencies = data[0]['currencies']
            data_continents = data[0]['region']
            data_languages = data[0]['languages']
            data_neighbors = data[0]['borders']
            data_maps = data[0]['maps']['googleMaps']
            data_population = data[0]['population']
            
            url_flag_png = data[0]['flags']['png']
            response_png = requests.get(url_flag_png).content
            with open("flag.png", "wb") as photo_flag:
                photo_flag.write(response_png)
                
            data_flag = data[0]['flags']['alt']
            
            url_coatOfArms = data[0]['coatOfArms']['png']
            response_arms = requests.get(url_coatOfArms).content
            with open("arm.png", "wb") as photo:
                photo.write(response_arms)
            
            print("government country📣 => ",data_government)
            print("capital🗿 => ",*data_capital)
            print("currencies💲 => ", data_currencies)
            print("continents 🌏 => ", data_continents)
            print("languages💭 => ", data_languages)
            print("neighbors👥 => ", *data_neighbors)
            print("maps 🗺 => ", data_maps)
            print("population🗣 => ", data_population)
            print("text flag🔲 => ", data_flag)
            print("photo save✔")
            
    if start == "exit":
        print("god bay💕")
        break