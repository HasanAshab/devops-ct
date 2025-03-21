# --- Base Stage ---
FROM python:3.11.4-slim-buster as base

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

# --- Development Stage ---
FROM base AS dev
RUN apt-get install git

COPY . .
RUN sed -i 's/\r$//g' /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# ... TODO

ENTRYPOINT ["/bin/bash", "/app/entrypoint.sh"]


# --- Production Stage ---
FROM base AS prod

COPY . .
RUN sed -i 's/\r$//g' /app/entrypoint.sh
RUN chmod +x /app/entrypoint.prod.sh

RUN groupadd -r user && useradd -r -g user appuser
USER appuser

ENTRYPOINT ["/bin/bash", "/app/entrypoint.prod.sh"]