#!/bin/sh

cd ${0%/*}
root=$(pwd)

git pull

cd backend
pipenv install --deploy
pipenv run python3 manage.py collectstatic --noinput
pipenv run python3 manage.py migrate

cd "$root"
cd frontend

npm install
npm run build