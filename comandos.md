python3 -m venv .venv
source .venv/bin/activate
pip install Django
django-admin startproject womakers
cd womakers/
python manage.py startapp surveys