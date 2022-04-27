#!bin/sh

python manage.py collectstatic
gunicorn Eshop.wsgi:application --bind :8000
