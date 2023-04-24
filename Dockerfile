FROM python:3.10-slim-buster

WORKDIR /app

LABEL version="3.9" maintainer="Charles Okeke okekecharles91@gmail.com"

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

COPY . .

EXPOSE 8000

CMD [ "python", "manage.py", "migrate", "&&", "python", "manage.py", "runserver" ]

