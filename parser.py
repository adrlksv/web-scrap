from bs4 import BeautifulSoup
import requests
from database.database_creat import Database, create_db


headers = {
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}


def generate_url_product() -> str:
    for count in range(1, 6):
        main_url = f'https://brandshop.ru/muzhskoe/?sort=saleDESC&page={count}'

        response = requests.get(main_url, headers=headers)

        soup = BeautifulSoup(response.text, 'lxml')

        data = soup.find_all('div', class_='product-card')

        for product_info in data:
            product_url = r'https://brandshop.ru' + product_info.find('a', class_='product-card__link').get('href')
            yield product_url


def get_info_product():
    for url_of_product in generate_url_product():
        with Database().get_connection() as con:
            cur = con.cursor()
            new_response = requests.get(url_of_product, headers=headers)

            new_soup = BeautifulSoup(new_response.text, 'lxml')

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

            cur.execute('''
                INSERT INTO products (brand, img_url, product_type, price, description, product_link)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (brand, img_url, product_type, price, description, product_link))

            con.commit()


def main():
    create_db()

    get_info_product()


if __name__ == "__main__":
    main()

