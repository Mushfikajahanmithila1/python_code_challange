import requests

api_key = "cf8b9c050fa34fe6a405d5fa94553856"

url = "https://newsapi.org/v2/top-headlines"

params = {
    "country": "us",
    "category": "technology",
    "apiKey": api_key
}

response = requests.get(url, params=params)

data = response.json()

if data["status"] == "ok":
    articles = data["articles"]

    for article in articles:
        print("Title:", article["title"])
        print("Source:", article["source"]["name"])
        print("URL:", article["url"])
        print("-" * 50)
else:
    print("Error:", data.get("message"))