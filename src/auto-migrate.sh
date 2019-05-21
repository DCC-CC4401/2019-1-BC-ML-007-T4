#!/usr/bin/env bash

source ../venv/bin/activate

python3 manage.py makemigrations users
python3 manage.py migrate
python3 manage.py makemigrations courses
python3 manage.py migrate
python3 manage.py makemigrations presentations
python3 manage.py migrate
python3 manage.py makemigrations rubrics
python3 manage.py migrate
