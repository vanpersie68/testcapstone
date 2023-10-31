from python:3

env pythonumbuffered=1

workdir /backend
copy ./backend/requirements.txt requirements.txt
run python3 -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ -r requirements.txt

copy ./backend .
copy ./backend/conf/docker.py 
# conf/env.py

cmd ["daphne", "-b", "0.0.0.0", "-p", "8000", "django_core.asgi:application"]
