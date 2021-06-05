#!/usr/bin/env bash

cd project

if [ ! -f manage.py ]; then
    git clone https://git.withthe.fish/paul/storage.git .
    python manage.py migrate
    python manage.py makestatic
else
    git pull
    python manage.py migrate
    python manage.py makestatic
fi

exec "$@"