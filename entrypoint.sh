#!bin/sh

gunicorn Eshop.wsgi:application --bind :8000
