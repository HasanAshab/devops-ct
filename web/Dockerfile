FROM python:3.11.4-slim-buster

WORKDIR /app
RUN pip install --upgrade pip


COPY ./requirements.txt .
RUN pip install -r requirements.txt


COPY . .
RUN sed -i 's/\r$//g' /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh


ENTRYPOINT ["/bin/bash", "/app/entrypoint.sh"]