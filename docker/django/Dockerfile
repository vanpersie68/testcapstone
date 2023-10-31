from python:3

env pythonumbuffered=1

workdir /backend
copy ./backend/requirements.txt requirements.txt

run pip install -r requirements.txt
run python manage.py migrate
run python manage.py runserver 0.0.0.0:8000
# run python3 -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ -r requirements.txt

copy ./backend .

cmd ["daphne", "-b", "0.0.0.0", "-p", "8000", "django_core.asgi:application"]
