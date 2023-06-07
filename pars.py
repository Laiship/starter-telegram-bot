import requests
from bs4 import BeautifulSoup
import random as rnd


def photo():
    page_number = rnd.randint(0, 7278)

    url = f'https://anime-pictures.net/posts?page={page_number}&order_by=date&ldate=0&lang=ru'
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ru,en;q=0.9',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 YaBrowser/23.5.1.714 Yowser/2.5 Safari/537.36'
    }
    response = requests.get(url=url, proxies={"http": "proxy.server:3128"}, headers=headers)
    link = []
    bs = BeautifulSoup(response.text, 'lxml')
    for links in bs.find_all('img', class_='svelte-1ibbyvk'):
        link.append(links.get('src'))
    return 'https:' + rnd.choice(link)
# pars_url = response.get(url='https://wallpaperscraft.ru/catalog/anime/page1', headers=headers)
# print(pars_url.ok)

# https://wallpaperscraft.ru/catalog/anime/page2

