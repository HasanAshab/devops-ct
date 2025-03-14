FROM python:3.12 AS builder
WORKDIR /app

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./entrypoint.sh .
RUN chmod +x /app/entrypoint.sh

COPY . .
ENTRYPOINT ["/app/entrypoint.sh"]