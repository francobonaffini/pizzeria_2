#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python pizza_project/manage.py collectstatic --no-input
python pizza_project/manage.py migrate