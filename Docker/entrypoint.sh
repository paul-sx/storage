#!/usr/bin/env bash

cd project

if [ ! -f manage.py ]; then
    git clone https://github.com/paul-sx/storage.git .
    python manage.py migrate --noinput
    python manage.py collectstatic --noinput
else
    git pull
    python manage.py migrate --noinput
    python manage.py collectstatic --noinput
fi

exec "$@"