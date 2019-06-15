#!/bin/bash

echo "Collect static files"
python manage.py collectstatic --noinput

echo "Apply database migrations"
python manage.py makemigrations
python manage.py migrate

echo "Starting server"
python manage.py runserver_plus 0.0.0.0:8000
