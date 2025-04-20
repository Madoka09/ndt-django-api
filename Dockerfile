FROM python:3.13-slim

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip \
    && pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-root

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]