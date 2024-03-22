#!/bin/sh

cd ${0%/*}
root=$(pwd)

export $(cat .env | xargs)

eval "$(ssh-agent -s)"
ssh-add "$1"

systemctl stop gunicorn
systemctl stop nginx

git pull origin main

cd backend

rm -f Pipfile.lock
rm -f requirement.txt
rm -rf static/*

pipenv install --deploy
pipenv run python3 manage.py migrate
pipenv run python3 manage.py test
pipenv run python3 manage.py import_tags
pipenv run python3 manage.py collectstatic --noinput

pipenv run pip freeze > requirement.txt
pip install -r requirement.txt

cd "$root"
cd frontend

npm install
npm run build

systemctl start gunicorn
systemctl start nginx