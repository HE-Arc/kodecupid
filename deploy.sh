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

sudo rm -f Pipfile.lock
sudo rm -rf static/*

pip install -r requirements.txt

python manage.py migrate
python manage.py import_tags
python manage.py spectacular --file schema.yml
python manage.py collectstatic --noinput

cd "$root"
cd frontend

npm install
npm run build

sudo systemctl start nginx
sudo systemctl start gunicorn