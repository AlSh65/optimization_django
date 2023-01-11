FROM python:3.9-alpine3.16

COPY requirements.txt /temp/requirements.txt
COPY django_service /django_service
WORKDIR /django_service
EXPOSE 8000

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password django_service-user

USER django_service-user