FROM python:3.9-slim

WORKDIR /app

COPY ./Flask_Service /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
