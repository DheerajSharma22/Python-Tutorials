# News app.

import json
import requests


print("Welcome to the DNews. Here you get latest news from different sources.")

searchQuery = input("\nEnter the keyword you want to know the news about :- ")


res = requests.get(f"https://newsapi.org/v2/everything?q={searchQuery}&apiKey=ENTER_API_KEY")

results = json.loads(res.text)

articles = results["articles"]

for article in articles:
    print(f"Source: {article["source"]["name"]}")
    print(f"Title: {article["title"]}")
    print(f"Description: {article["description"]}")
    print(f"Url: {article["url"]}")
    print("\n")