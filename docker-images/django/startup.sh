#!/bin/sh
cd /files

rm -f Pipfile.lock
pipenv install --deploy --python "/usr/bin/python3"

while [ true ];
do
    pipenv run python3 manage.py spectacular --file schema.yml
    pipenv run python3 manage.py collectstatic --noinput
    pipenv run python3 manage.py migrate
    pipenv run python3 manage.py runserver 0.0.0.0:$KODECUPID_BACKEND_PORT
done

