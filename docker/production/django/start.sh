#!/bin/bash

echo "Collect static files"
python manage.py collectstatic --noinput

echo "Apply database migrations"
python manage.py makemigrations
python manage.py migrate

echo "Starting server"
gunicorn --bind :8000 --reload config.wsgi:application
