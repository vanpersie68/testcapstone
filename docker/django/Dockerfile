from python:3

env pythonumbuffered=1

workdir /backend
copy ./backend/requirements.txt requirements.txt

run python -m pip install -r requirements.txt
# run python3 -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ -r requirements.txt

copy ./backend .

# cmd ["daphne", "-b", "0.0.0.0", "-p", "8000", "django_core.asgi:application"]
# cmd ["0.0.0.0", "-p", "8000", "django_core.asgi:application"]
cmd ["python", "manage.py", "runserver", "0.0.0.0:8080"]