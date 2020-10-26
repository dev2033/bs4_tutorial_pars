import requests
from bs4 import BeautifulSoup
import json


"""Собираем ссылки пользователей
    (далее код нужно закоментировать)
"""

# persons_url_list = []
#
# for i in range(0, 740, 20):
#     url = f'https://www.bundestag.de/ajax/filterlist/en/members/453158-453158/h_a45203fd0f1592191f1bda63b5d86d72?limit=20&noFilterSet=true&offset={i}'
#
#     q = requests.get(url)
#     result = q.content
#
#     soup = BeautifulSoup(result, 'lxml')
#     persons = soup.find_all(class_='bt-open-in-overlay')
#
#     for person in persons:
#         person_page_url = person.get('href')
#         persons_url_list.append(person_page_url)
#
# with open('persons_url_list.txt', 'a') as file:
#     for line in persons_url_list:
#         file.write(f'{line}\n')

"""
Далее работаем с файлом persons_url_list, 
чтобы не бомбить сайт запросами
"""

with open('persons_url_list.txt') as file:

    lines = [line.strip() for line in file.readlines()]

    # Список для наполнения данными json файл
    data_dict = []
    count = 0

    for line in lines:
        q = requests.get(line)
        result = q.content

        soup = BeautifulSoup(result, 'lxml')
        person = soup.find(class_='bt-biografie-name').find('h3').text
        # Разделяем строку методом split() - разделителем является запятая
        person_name_company = person.strip().split(',')
        # Теперь переменная person_name_company состоит из 2х элементов
        # вызываем их обращаясь к ним по индексу, 
        # у person_company надо убрать отступы методом strip()
        person_name = person_name_company[0]
        person_company = person_name_company[1].strip()

        # Собираем социальные сети
        social_networks = soup.find_all(class_='bt-link-extern')
        # Создаем пустой список социльных сетей пользователей,
        # Далее мы его наполняем, используя цикл
        social_networks_urls = []
        for item in social_networks:
            social_networks_urls.append(item.get('href'))

        data = {
            'person_name': person_name,
            'company_name': person_company,
            'social_networks': social_networks_urls
        }
        # С каждой итерацией цикла, будет идти счетчик
        count += 1
        print(f'#{count}: {line} is done!')

        data_dict.append(data)
        # файл data.json наполняем списком data с помощью 
        # метода dump, так же передаем параметр 
        # indent=4 для красивого отображения json
        with open('data.json', 'w') as json_file:
            json.dump(data_dict, json_file, indent=4)
