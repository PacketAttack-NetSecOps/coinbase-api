FROM python:3.12-slim

COPY ./src /app

WORKDIR /app

RUN pip install --no-cache-dir -r /app/requirements.txt && rm /app/requirements.txt

CMD python3 /app/main.py