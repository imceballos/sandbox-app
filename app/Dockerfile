FROM python:3.11.1-slim

COPY app/requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install --upgrade -r /app/requirements.txt

COPY ./app /app

