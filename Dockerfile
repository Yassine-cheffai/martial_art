# pull official base image
FROM python:3.7.0-alpine

# set work directory
WORKDIR /usr/src/martial

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN apk --update add \
    build-base \
    jpeg-dev \
    zlib-dev \
    sudo \
    bash \
    poppler \
    tesseract-ocr

RUN apk add poppler-utils

# install dependencies
RUN pip install --upgrade pip
RUN pip install psycopg2-binary
COPY ./requirements.txt /usr/src/requirements.txt
RUN pip install -r ../requirements.txt

