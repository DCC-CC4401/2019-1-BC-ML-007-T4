#!/usr/bin/env bash

source ../venv/bin/activate

python3 manage.py makemigrations users
python3 manage.py migrate
python3 manage.py makemigrations
python3 manage.py migrate
