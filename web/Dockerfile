# --- Base Stage ---
FROM python:3.11.4-slim-buster as base
WORKDIR /app

RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN sed -i 's/\r$//g' /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh


# --- Development Stage ---
FROM base AS dev
RUN apt-get install git
# ... TODO

# --- Production Stage ---
FROM base AS prod
RUN groupadd -r user && useradd -r -g user appuser
USER appuser

ENTRYPOINT ["/bin/bash", "/app/entrypoint.sh"]

