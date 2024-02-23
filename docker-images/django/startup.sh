#!/bin/sh
cd /files

pipenv install --deploy --python "/usr/bin/python3"

pipenv run python3 manage.py migrate
pipenv run python3 manage.py runserver 0.0.0.0:5173