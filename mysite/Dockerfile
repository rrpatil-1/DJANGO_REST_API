# syntax=docker/dockerfile:1.4

FROM --platform=$BUILDPLATFORM python:3.10-alpine as builder
EXPOSE 8000
WORKDIR /app

#install system dependencies

RUN apk update
RUN apk add \
    pkgconfig \
    gcc \
    musl-dev \
    bash \
    mariadb-dev

#install package from requirement.txt
COPY requirement.txt /app
RUN pip install --no--cache--dir -r requirement.txt

#copy the current dir contents into the container at /usr/src/app
COPY ./app

# run server
ENTRYPOINT ['python3']
CMD ["manage.py","runserver","0.0.0.0:8000"]
