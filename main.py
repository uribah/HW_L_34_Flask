
'''
Задание Lite

1. Создать 3 html формы (можно взять из выполненного дз к 13-му вебинару): главная

страницы, страница с парсером, данные о вас.

2. Наполнение главной страницы и страницы с данными оставить на Ваше

усмотрение.

3. На странице с парсером реализовать интерфейс с пользователем. Например, по

нажатию кнопки осуществляется парсинг выбранного Вами портала, после чего

выводится некоторая информация о результатах парсинга.

'''

from flask import Flask, render_template , request
from bs4 import BeautifulSoup
import requests

def parsing():
  URL_ = 'https://auto.ria.com/reviews/volvo/v40/'

  page_ = requests.get(URL_)
  # print(page_.status_code)

  soup_ = BeautifulSoup(page_.text, 'html.parser')

  reviews_ = soup_.find_all('div', class_='reviews-car-cardi-top')

  pars_txt = []
  for rev in reviews_:
    # print(rev.text)
    pars_txt.append(rev.text)

  return pars_txt

# print(parsing()[0])

app = Flask(__name__)

@app.route('/')
@app.route('/main')
def home():
  return render_template('main.html')

@app.route('/form_2')
def form_2():
  return render_template('form_2.html')
  
@app.route('/form_3',  methods = ['POST'])
def form_3():
  # txt = "ПРобный текс"
  q_1 = request.form['question']

  full_txt = parsing()
  txt_1 = full_txt[0]

  return render_template('form_3.html', question=q_1, txt=txt_1)

if __name__ == "__main__":
  app.run()
