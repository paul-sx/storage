#!/usr/bin/env bash

cd project

if [ ! -f manage.py ]; then
    git init
    git remote add origin https://github.com/paul-sx/storage.git
    git fetch
    git reset --hard origin/main
    python manage.py migrate --noinput
    python manage.py collectstatic --noinput
    python manage.py rebuild_index --noinput
else
    git pull
    python manage.py migrate --noinput
    python manage.py collectstatic --noinput
    python manage.py rebuild_index --noinput
fi

exec "$@"