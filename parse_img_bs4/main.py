from urllib.request import urlretrieve

import requests
from bs4 import BeautifulSoup

url = "http://simfpolyteh.ru/raspisanie/"

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) "
                  "Version/11.0 Mobile/15A5341f Safari/604.1 "
}

req = requests.get(url, headers=headers)
src = req.text

soup = BeautifulSoup(src, "lxml")


def pars_img():
    """Берет картинку с сайта"""
    try:
        image = soup.find(class_="page_raspis_block_img").find("img").get("src")
        urlretrieve(image, filename="penis.png")
        print("Скачивание успешно завершено")
    except Exception:
        print("Не удалось скачать!!!")


if __name__ == '__main__':
    pars_img()
