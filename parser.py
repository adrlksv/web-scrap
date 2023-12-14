from bs4 import BeautifulSoup
import requests
from database.db import Database


headers = {
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}


d_base = Database()  # Создаём экземпляр класса Database ля работы с базой данных


def generate_url_product() -> str:
    for count in range(1, 6):
        main_url = f'https://brandshop.ru/muzhskoe/?sort=saleDESC&page={count}'

        response = requests.get(main_url, headers=headers)  # Отправляем HTTP-запрос к странице

        soup = BeautifulSoup(response.text, 'lxml')  # Создаем объект BeautifulSoup для парсинга HTML-кода страницы

        data = soup.find_all('div', class_='product-card')   # Находим все блоки с информацией о продуктах

        for product_info in data:
            product_url = r'https://brandshop.ru' + product_info.find('a', class_='product-card__link').get('href')
            yield product_url  # Генерируем URL каждого продукта


def get_info_product():
    if d_base.has_data():
        d_base.clear_data()  # Если в базе данных есть данные, удаляем их
    for url_of_product in generate_url_product():
        with d_base.get_connection() as con:
            cur = con.cursor()  # Создаём объект курсора для выполнения SQL запросов

            new_response = requests.get(url_of_product, headers=headers)  # Отправляем HTTP-запрос к странице товара

            new_soup = BeautifulSoup(new_response.text, 'lxml')  # Создаем yjdsq объект BeautifulSoup для парсинга HTML-кода товара

            # Извлекаем информацию о товаре
            brand = new_soup.find('h1').find('a').text
            img_url = new_soup.find('div', class_='product-page__img _ibg').find('img').get('src')
            product_type = new_soup.find('h1').find('span').text.strip()
            product_link = url_of_product
            price = new_soup.find('div', class_='product-order__price').find('meta').get('content') + 'р.'
            description_data = new_soup.find('div', class_='product-menu__content')
            description_all = description_data.find_all('li')

            description_list = []
            for description_html in description_all:
                description_el = description_html.text.strip()
                description_list.append(description_el)

            description = '; '.join(description_list)

            # Записываем информацию в базу данных
            cur.execute('''
                INSERT INTO products (brand, img_url, product_type, price, description, product_link)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (brand, img_url, product_type, price, description, product_link))

            con.commit()
