#!bin/sh

gunicorn Eshop.wsgi:application --bind :5000
