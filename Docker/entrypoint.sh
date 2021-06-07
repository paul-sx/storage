#!/usr/bin/env bash

cd project

if [ ! -f manage.py ]; then
    git clone https://github.com/paul-sx/storage.git .
    python manage.py migrate
    python manage.py collectstatic
else
    git pull
    python manage.py migrate
    python manage.py collectstatic
fi

exec "$@"