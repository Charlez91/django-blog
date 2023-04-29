FROM python:3.10-slim-buster

LABEL version="3.9" maintainer="Charles Okeke okekecharles91@gmail.com"


ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

RUN set -e;\
    chmod +x entrypoint.sh;

EXPOSE 8000

ENTRYPOINT [ "entrypoint.sh" ]

