release: python manage.py migrate --noinput
web: gunicorn --bind :$PORT config.wsgi:application
