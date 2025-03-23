# --- Base Stage ---
FROM python:3.11.4-slim-buster AS base

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN sed -i 's/\r$//g' entrypoint.sh entrypoint.prod.sh && \
    chmod +x entrypoint.sh entrypoint.prod.sh


# --- Development Stage ---
FROM base AS dev
RUN apt-get update && apt-get install -y --no-install-recommends git && \
    rm -rf /var/lib/apt/lists/*

# ... TODO

ENTRYPOINT ["/bin/bash", "/app/entrypoint.sh"]


# --- Production Stage ---
FROM base AS prod

RUN addgroup --system app && adduser --system --group app && \
  chown -R app:app /app

USER app

ENTRYPOINT ["/bin/bash", "/app/entrypoint.prod.sh"]