from bs4 import BeautifulSoup
import requests
import json


def hd_rezka():
    url = 'https://hdrezka.re/novinki-ordinary/'
    # url = 'https://hdrezkanbnssf.net/new/'
    HEADERS = {
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }

    r = requests.get(url, headers=HEADERS)

    soup = BeautifulSoup(r.text, 'lxml')
    items = soup.find_all('div', class_='b-content__inline_item')

    new_dict = {}
    for item in items:
        url_id = item.find('div', class_='b-content__inline_item-link').find('a').get('href')
        title = item.find('div', class_='b-content__inline_item-link').get_text()
        link = item.find('div', class_='b-content__inline_item-link').find('a').get('href')
        movie_img = item.find('div', class_='b-content__inline_item-cover').find('img').get('src')

        item_id = url_id.split('/')[-1]
        item_id = item_id[:-5]

        new_dict[item_id] = {
            'title': title,
            'link': link,
            'movie_img': movie_img
        }

    with open('new_dict.json2', 'w', encoding='utf-8') as file:
        json.dump(new_dict, file, indent=3, ensure_ascii=False)

def check_film_updet():
    with open("new_dict.json", encoding="utf-8") as file:
        new_dict = json.load(file)

   # url = 'https://hdrezkanbnssf.net/new/'
    url = 'https://hdrezka.re/novinki-ordinary/'
    HEADERS = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }

    r = requests.get(url, headers=HEADERS)

    soup = BeautifulSoup(r.text, 'lxml')
    items = soup.find_all('div', class_='b-content__inline_item')

    fresh_film = {}
    for item in items:
        url_id = item.find('div', class_='b-content__inline_item-link').find('a').get('href')
        item_id = url_id.split('/')[-1]
        item_id = item_id[:-5]

        if item_id in new_dict:
            continue
        else:
            title = item.find('div', class_='b-content__inline_item-link').get_text()
            link = item.find('div', class_='b-content__inline_item-link').find('a').get('href')
            movie_img = item.find('div', class_='b-content__inline_item-cover').find('img').get('src')

            new_dict[item_id] = {
                'title': title,
                'link': link,
                'movie_img': movie_img
            }

            fresh_film[item_id] = {
                'title': title,
                'link': link,
                'movie_img': movie_img
            }

    with open('new_dict.json', 'w', encoding='utf-8') as file:
        json.dump(new_dict, file, indent=3, ensure_ascii=False)

    return fresh_film

def main():
    hd_rezka()
    print(check_film_updet())

if __name__ == '__main__':
    main()









