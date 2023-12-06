![Project Brandshop logo](images/Logo.png)
# BRANDSHOP

![Python](https://img.shields.io/badge/Python_3.10-blue?logo=python&logoColor=yellow)
![SQLite](https://img.shields.io/badge/SQLite-purple?logo=SQLite&logoColor=blue)
![Docker](https://img.shields.io/badge/Docker-grey?logo=Docker&logoColor=blue)
![DockerCompose](https://img.shields.io/badge/DockerCompose-blue)
![Static Badge](https://img.shields.io/badge/FastAPI-black?logo=FastAPI)







Данный парсер предназначен для сбора информации о товарах, отсортированных по убыванию скидки, на сайте одежды Brandshop. Это позволит пользователю быстро посмотреть какие вещи с наибольшкй выгодой он может купить на данном сайте.



###### Информация, которая будет парситься с этого сайта:
- Вид товара(футболка, кроссовки и тд.)
- Цена товара
- Описание товара(страна производителя, материал и тд.)
- Ссылка на фото товара
- Ссылка на товар


###### Структура проекта
    │
    ├── backend (часть с FastAPI)
    │   └── b_app.py
    │
    ├── database
    │   └── database_create.py
    │
    ├── main.py
    └── parser.py



### Установка и настройка
###### Клонируем репозиторий:
    git clone https://github.com/adrlksv/web-scrap.git

###### Переходим в директорию проекта 
    cd web-scrap

###### Сборка и запуск контейнеров Docker
    docker-compose up --build


### Ссылка, с которой работает парсер:
    https://brandshop.ru/muzhskoe/?sort=saleDESC

