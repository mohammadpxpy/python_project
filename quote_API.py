import requests

url = "https://zenquotes.io/api/random"
respons = requests.get(url)

if respons.status_code == 200:
    start = input("for start click Enter")
    if len(start) == 0:
        data = respons.json()
        
        quote = data[0]['q']
        
        from_person = data[0]['a']
        
        definition = data[0]['h']
        
        print(f"quote💌 : {quote}")
        print(f"from🗣 {from_person}")
        print(f"💬 : {definition}".replace("<blockquote>&ldquo;", "").replace("&rdquo; &mdash; <footer>", "").replace("</footer></blockquote>", ""))