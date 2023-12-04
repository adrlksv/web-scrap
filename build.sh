#!/bin/bash

# Сборка Docker-образа
docker-compose build

# Запуск сервисов
docker-compose up -d

echo "Сервис теперь работает по адресу http://128.0.0.1:8080/"
