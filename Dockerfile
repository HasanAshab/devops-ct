FROM python:3.12 AS builder
WORKDIR /app

RUN chmod +x /app/entrypoint.sh
RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt


FROM gcr.io/distroless/python3-debian12
WORKDIR /app

COPY --from=builder . .

ENTRYPOINT ["/app/entrypoint.sh"]
