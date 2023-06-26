#!/usr/bin/env bash
# exit on error
set -o errexit

poetry install

python manage.py collectstatic --no-input
python manage.py flush
python manage.py loaddata data.json
python manage.py migrate