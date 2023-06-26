#!/usr/bin/env bash
# exit on error
set -o errexit

poetry install

python manage.py collectstatic --no-input
python manage.py flush --no-input
python manage.py loaddata data.json
python manage.py migrate --no-input