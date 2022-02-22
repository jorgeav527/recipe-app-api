FROM python:3.8-alpine
LABEL maintainer="jorgeav527@gmail.com"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-deps \
    build-base postgresql-dev musl-dev linux-headers zlib-dev jpeg-dev && \
    /py/bin/pip install -r /requirements.txt && \
    apk del .tmp-deps && \
    adduser --disabled-password --no-create-home user

RUN mkdir /app
WORKDIR /app
COPY ./app /app

ENV PATH="/py/bin:$PATH"

USER user