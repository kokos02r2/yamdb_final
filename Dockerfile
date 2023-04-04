FROM python:3.7-slim

RUN apt-get update && apt-get install -y libpq-dev gcc

WORKDIR /app

COPY api_yamdb/requirements.txt /app

RUN pip3 install -r /app/requirements.txt --no-cache-dir

COPY ./ /app

CMD ["gunicorn", "api_yamdb/api_yamdb.wsgi:application", "--bind", "0:8000" ]