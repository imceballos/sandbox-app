FROM python:3.11.1-slim

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ENV TZ=America/Santiago

COPY ./src /usr/src/app
COPY ./requirements.txt /usr/src/app/requirements.txt

RUN pip install --upgrade -r requirements.txt

CMD ["gunicorn", "--bind=0.0.0.0:5000", "--workers=4", "manage:app"]

