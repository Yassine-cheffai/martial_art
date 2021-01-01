FROM python:3.7.0-alpine

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

WORKDIR /app/mart
COPY requirements.txt /app/mart
RUN pip install --upgrade pip
RUN pip install psycopg2-binary
RUN pip install -r requirements.txt

EXPOSE 8150
CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8150"]