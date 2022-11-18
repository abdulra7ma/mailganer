#!/bin/sh

docker-compose --file docker-compose-server.yml --project-name=quran_kg up --build -d
docker exec --user root -it quran_kg_app_1 fab django.migrate
docker exec --user root -it quran_kg_app_1 fab django.collectstatic
