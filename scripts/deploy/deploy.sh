#!/bin/sh

docker-compose --file docker-compose-server.yml --project-name=mailganer up --build -d
docker exec --user root -it mailganer_app_1 python app/manage.py makemigrations
docker exec --user root -it mailganer_app_1 python app/manage.py migrate
docker exec --user root -it mailganer_app_1 python app/manage.py collectstatic
