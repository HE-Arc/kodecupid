#!/bin/sh

cd ${0%/*}
root=$(pwd)

export $(cat .env | xargs)

eval "$(ssh-agent -s)"
ssh-add "$1"

sudo systemctl stop gunicorn
sudo systemctl stop nginx

git pull origin main

cd backend

rm -f Pipfile.lock
rm -f requirement.txt
rm -rf static/*

sudo pipenv install --deploy
sudo pipenv run python3 manage.py migrate

sudo pipenv run python3 manage.py import_tags

sudo pipenv run python3 manage.py spectacular --file schema.yml
sudo pipenv run python3 manage.py collectstatic --noinput

sudo pipenv run pip freeze > requirement.txt
pip install -r requirement.txt

cd "$root"
cd frontend

npm install
npm run build

sudo systemctl start nginx
sudo systemctl start gunicorn