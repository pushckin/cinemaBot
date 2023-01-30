import json

with open("new_dict.json", encoding="utf-8") as file:
    news_dict = json.load(file)


search_id = '5476001-sezon-kkok-tu-2023'

if search_id in news_dict:
    print("новость есть")
else:
    print("добавте новость")