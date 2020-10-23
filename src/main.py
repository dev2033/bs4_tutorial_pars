import re

from bs4 import BeautifulSoup

# открываем файл на открытие

with open("blank/index.html") as file:
    src = file.read()

# обозначаем объект

soup = BeautifulSoup(src, "lxml")

# вызываем тег title из html

# title = soup.title
# print(title.text)  # вызываем метод текст, для отображения текста без тега
# print(title.string)  # вызываем строку, для отображения текста без тега

"""Методы find() и find_all()"""
# page_h1 = soup.find("h1")   # выводит тег h1 -> первый по порядку
# print(page_h1)
#
# page_h1_all = soup.find_all("h1")   # выводит все теги h1 из кода
# print(page_h1_all)
#
# for item in page_h1_all:    # цикл, перебирающий page_h1_all, который выводит
#     print(item.text)        # весь текст тегов h1 без <h1></h1>

# тут получаем div с классом user__name
# выводим user_name, передаем параметр text и strip(), который убирает все
# пробелы, оставшиеся от класса div

# user_name = soup.find("div", class_="user__name")
# print(user_name.text.strip())

# так же можно искать делее по тегам

# user_name = soup.find("div", class_="user__name").find("span").text
# print(user_name)

# так же для передачи параметров по поиску можно передать словарь

# user_name = soup.find("div", {"class": "user__name"}).find("span").text
# print(user_name)

# find_all_spans_in_user_info = soup.find(class_="user__info").find_all("span")
# print(find_all_spans_in_user_info)

# for item in find_all_spans_in_user_info:
#     print(item.text)

# так как find_all - это список, можно обращаться по их индексу и применять
# методы soup()

# print(find_all_spans_in_user_info[0].text)

# парсим ссылки социальных сетей

# social_links = soup.find(class_="social__networks").find("ul").find_all("a")
# print(social_links)

# all_a = soup.find_all("a")

# пробегаем по всем ссылкам и выводим текст ссылки и саму ссылку

# for item in all_a:
#     item_text = item.text
#     item_url = item.get("href")
#     print(f'{item_text} - {item_url}')


"""Методы find_parent() и find_parents"""

# find_parent() - выбирает блок до первого родителя (1), если нечего не
# указывать
# если что-то передать в этот метот, он найдет тот класс(тот элемент) который
# вы укажите ему(2)

# (1)
# post_dev = soup.find(class_="post__text").find_parent()
# print(post_dev)

# (2)
# post_dev = soup.find(class_="post__text").find_parent("div", "user__post")
# print(post_dev)


# find_parents() - выбирает блок от какого-то определенного места и до конца,
# ему также можно ставить параметры для поиска и ограничитель(до какого
# момента парсить html)

# post_divs = soup.find(class_="post__text").find_parents("div", "user__post")
# print(post_divs)
# for item in post_divs:
#     item_text = item.text
#     print(item_text.strip())


"""
Методы next_element(`s) -> find_element и previous_element(`s)
"""

# Тут происходит обращение к классу post__title, а затем к его следующему
# элементу, почему мы обратились 2 раза? -> next_element учитавает перенос
# строки. У него есть похожий метод find_next, который сразу возвращает
# следующий элемент

# next_el = soup.find(class_="post__title").next_element.next_element.text
# print(next_el)

# next_el = soup.find(class_="post__title").find_next().text
# print(next_el)


"""Методы find_next_sibling() и  find_previous_sibling"""

# find_next_sibling - выдает последний пост статьи (div)

# next_sib = soup.find(class_="post__title").find_next_sibling()
# print(next_sib)

# find_previous_sibling - выдает предыдущий пост статьи (div)

# prev_sib = soup.find(class_="post__title").find_previous_sibling()
# print(prev_sib)


"""
Регулярные выражения (модуль - 're').
Поиск по тексту
"""

# тут происходит поиск по слову одежда(исключительно в тегах a) с большой буквы

# find_a_by_text = soup.find("a", text=re.compile("Одежда"))
# print(find_a_by_text)

# тут происходит поиск слова одежда во всем коде, в верхнем и нижнем регистре

# find_all_clothes = soup.find_all(text=re.compile("[Оо]дежда"))
# print(find_all_clothes)

