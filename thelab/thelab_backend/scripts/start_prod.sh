#!/bin/bash

python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate --no-input
gunicorn thelab.wsgi -b 0.0.0.0:8000