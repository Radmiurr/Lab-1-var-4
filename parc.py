from bs4 import BeautifulSoup # импортируем библиотеку BeautifulSoup
import requests # импортируем библиотеку requests

def parse():
    url = "https://auto.drom.ru/all/#tabs" # передаем необходимы URL адрес
    page = requests.get(url) # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
    print(page.status_code) # смотрим ответ
    soup = BeautifulSoup(page.text, "html.parser") # передаем страницу в bs4
    f = open('cars.txt','w+',encoding='utf-8')



    block = soup.findAll('a', class_="css-xb5nz8 e1huvdhj1") # находим  контейнер с нужным классом
    for data in block: # проходим циклом по содержимому контейнера
        z = data.text
        print(z)
        f.write(z.replace(' ', ' ') + "\n")

