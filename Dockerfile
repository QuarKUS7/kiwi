FROM python:3.6-alpine

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT ["python", "/app/kiwi_airports.py"]
