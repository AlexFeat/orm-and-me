# ./backend/Dockerfile

# Базовый образ = python3.10-buster
FROM python:3.10-slim
RUN pip install --upgrade pip

# копируем и уст. зависимости
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# уст. переменную окружения PYTHONUNBUFFERED чтобы логи fastapi не застревали в контейнере
ENV PYTHONUNBUFFERED 1
# Указываем путь до python модулей -> текущая директория, иначе будет ошибка
# backend_1   | ModuleNotFoundError: No module named 'src'
ENV PYTHONPATH=.

# не создавать .pyc файлы в контейнере
ENV PYTHONDONTWRITEBYTECODE 1

# Создаем рабочую диру под backend
WORKDIR /project

COPY ./src/migrations ./migrations
COPY ./src/alembic.ini .

COPY ./src/app ./app
COPY ./src/manage.py .

# RUN alembic upgrade head

CMD ["python", "manage.py", "runserver"]