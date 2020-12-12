import requests
import time
import fake_useragent

from bs4 import BeautifulSoup

from custom_logging import logger


user = fake_useragent.UserAgent().random

# создание сессии для сохранения куки, для того чтобы
# дальше не авторизовываться во время других запросов
session = requests.Session()

headers = {
    'user-agent': user
}

data = {
    'запрос_логин': 'логин',
    'запрос_пароль': 'пароль'
}

link = "https://..."

responce = session.get(link, data=data, headers=headers)

# создание куки списка для того чтобы в дальнейшем можно было
# его вызывать для авторизации
cookies_dict = [
    {"domain": key.domain, "name": key.name, "path": key.path,
     "value": key.value}
    for key in session.cookies
]

session2 = requests.Session()
for cookies in cookies_dict:
    session2.cookies.set(**cookies)

resp = session2.get()
