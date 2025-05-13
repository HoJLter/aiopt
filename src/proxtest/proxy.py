import asyncio

from aiohttp import ClientSession

import requests
from bs4 import BeautifulSoup


def get_free_proxies():
    url = "https://free-proxy-list.net/"

    try:
        # Получаем HTML страницы
        response = requests.get(url)
        response.raise_for_status()  # Проверяем на ошибки

        soup = BeautifulSoup(response.text, 'html.parser')

        # Ищем таблицу с прокси
        proxies_table = soup.find('table', {'class': 'table table-striped table-bordered'})

        if not proxies_table:
            print("Таблица с прокси не найдена!")
            return []

        proxies = []

        # Парсим строки таблицы (пропускаем заголовок)
        rows = proxies_table.find_all('tr')[1:]  # [1:] чтобы пропустить заголовок

        for row in rows:
            cols = row.find_all('td')
            if len(cols) >= 2:  # IP и порт есть в первых двух столбцах
                ip = cols[0].text.strip()
                port = cols[1].text.strip()
                proxy = f"{ip}:{port}"
                proxies.append(proxy)

        return proxies

    except Exception as e:
        print(f"Ошибка при парсинге прокси: {e}")
        return []





class Proxy:
    def __init__(self, proxies: list, url):
        self.proxies = proxies
        self.url = url


    @staticmethod
    async def check_proxy(proxy:str, session:ClientSession, url:str) -> tuple[bool,str]:
        try:
            async with session.get(url, proxy=proxy) as response:
                return True, proxy

                return False, proxy
        except Exception as e:
            print(e)
            return False, proxy


    async def check_proxies(self):
        async with ClientSession() as session:
            tasks = [self.check_proxy(proxy, session, self.url) for proxy in self.proxies]
            result = asyncio.gather(*tasks)
            return result


test_proxies = Proxy(["https://"+x for x in get_free_proxies()], url="https://google.com")


a = asyncio.run(test_proxies.check_proxies())
for res, proxy in a.result():
    if res:
        print(proxy)