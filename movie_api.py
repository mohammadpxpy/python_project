import requests


while True:
    try:
        user = input("<< exit >> Movie name: ")
        url = f"https://imdb.iamidiotareyoutoo.com/search?q={user}"
        response = requests.get(url)
        if response.status_code == 200:
                data = response.json()
                data_movie = data['description'][2]
                name_movie = data_movie['#TITLE']
                yaer_movie = data_movie['#YEAR']
                rank_movie = data_movie['#RANK']
                actors_movie = data_movie['#ACTORS']
                imdb_url = data_movie['#IMDB_URL']
                
                url_img = data_movie['#IMG_POSTER']
                img = requests.get(url_img).content
                with open("movie.jpg", "wb") as photo:
                    photo.write(img) 
                
                if user == "exit":
                    print("come again😘")
                    break
                
                print(name_movie)
                print("yaer: ",yaer_movie)
                print("rank => ",rank_movie)
                print("actors: ",actors_movie)
                print("web imbd => ",imdb_url)
                print("image save✔")
                
    except IndexError:
        print("plase chose thr right name!")
        continue

        
