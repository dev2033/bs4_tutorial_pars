"""
Парсинг аккаунта в инстаграме, собираем посты.
Аккаунт автора канала на ютуб - Диджитализируй.
Ссылка: https://www.youtube.com/channel/UC9MK8SybZcrHR3CUV4NMy2g
"""
from urllib.request import urlretrieve

import requests
import time

from bs4 import BeautifulSoup

from custom_logging import logger


url = "https://www.instagram.com/alexeygoloburdin/?hl=ru"

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) "
                  "AppleWebKit/604.1.34 (KHTML, like Gecko) "
                  "Version/11.0 Mobile/15A5341f Safari/604.1 "
}

req = requests.get(url, headers=headers)
src = req.text
#
# with open("html_page/index.html", "w") as file:
#     file.write(src)
#
# with open("html_page/index.html") as file:
#     src = file.read()


def main():
    soup = BeautifulSoup(src, "lxml")

    all_posts = soup.find_all("div", class_="KL4Bh")
    count = 0
    for item in all_posts:
        images = item.find("img").get("src")
        count += 1
        urlretrieve(images, filename=f"image/img.png")
        time.sleep(20)

    print("Завершено")


if __name__ == '__main__':
    main()

