# Credits to:
# https://github.com/docker/docker-py/blob/master/Dockerfile-py3

ARG PYTHON_VERSION=3.8

FROM python:${PYTHON_VERSION}

RUN mkdir /src
WORKDIR /src

COPY requirements.txt /src/requirements.txt
RUN pip install -r requirements.txt

RUN git config --global user.email "test@jwdunne.test"
RUN git config --global user.name "James W. Dunne"

COPY . /src
RUN pip install -e .
