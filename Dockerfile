FROM python:3.12

WORKDIR /src

COPY src/requirements.txt /src
RUN pip install -r requirements.txt


COPY src /src
