# Mailgaber

## Table of contents
- [Mailganer Task](#stripe-payment-task)
  - [Table of contents](#table-of-contents)
  - [Логика приложения](#app-logic)
    - [Main Tasks](#main-tasks)
  - [run in dev environment](#run-in-dev-environment)
  - [Run docker for production](#run-docker-for-production)
  - [run test files](#run-test-files)



## Логика приложения
подписаться на информационный бюллетень, а также возможность отправлять новый информационный бюллетень и возможность отправлять запланированный информационный бюллетень.

### how should it be used

#### - subscribe to newsletter
- url: http://127.0.0.1:8000/subscribe

#### - add a new newsletter
- url: http://127.0.0.1:8000/newsletter

#### - add a new scheduled newsletter
- url: http://127.0.0.1:8000/scheduled-newsletter

### Main Tasks
- [x] HTML-страница для подписки на рассылку
- [x] HTML-страница для отправки бюллетеня
- [x] HTML-страница для отправки запланированной рассылки
- [x] модели для получателя электронной почты
- [x] модели для рассылки
- [x] модели для запланированной рассылки
- [x] докеризовали приложение для среды разработки и производственной среды
  - добавлены gunicorn и nginx в файл yaml производственного докера
- [x] используемые переменные окружения
- [x] зарегистрированные модели в админке Django
- [x] отдельный уровень взаимодействия с БД для сервисов
- [x] Большая часть кода приложения задокументирована


## Run locally
> **_NOTE:_** этот проект использовал python 2.7.18 и pyenv в качестве менеджера среды

1. создать новый venv 
```shell
pyenv virtualenv 2.7.18 mailganer
```
2. активировать вновь созданный venv
```shell
pyenv activate mailganer
```
3. перенести базу данных
```shell
python app/manage.py migrate
```
4. запустить приложение
```shell
python app/manage.py runserver
```

## Run in docker
### run in a docker dev environment

1. изменить режим файла на выполнение
```
chmod +x scripts/local/start_dev.sh
```
2. запустить демон докера
```
sh scripts/local/start_dev.sh
```
3. остановить образ Docker
```
docker-compose down
```

### run docker for production

1. изменить режим файла на выполнение
``` shell
chmod +x scripts/deploy/deploy.sh
```
2. запустить демон докера
```shell
sh scripts/deploy/deploy.sh
```
3. остановить образ Docker
``` shell
docker-compose --file docker-compose-server.yml --project-name=mailganer down
```
- для удаления томов при остановке контейнеров
   ``` shell
   docker-compose --file docker-compose-server.yml --project-name=mailganer down -v --remove-orphans
   ```