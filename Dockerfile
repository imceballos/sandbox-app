FROM python:3.11.1-slim

RUN mkdir -p /usr/src/app
RUN pip install --upgrade pip
RUN apt-get update && apt-get install -y netcat && apt-get install -y git
WORKDIR /usr/src/app

ENV TZ=America/Santiago

COPY . /usr/src/app

RUN pip install -r requirements.txt

ENTRYPOINT ["./entrypoint.sh"]
