#!/bin/sh

cd ${0%/*}
root=$(pwd)

export $(cat .env | xargs)

eval "$(ssh-agent -s)"
ssh-add "$1"

git pull origin main

cd backend
pipenv install --deploy
pipenv run python3 manage.py collectstatic --noinput
pipenv run python3 manage.py migrate

cd "$root"
cd frontend

npm install
npm run build