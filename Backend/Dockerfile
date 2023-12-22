FROM python:3.9-slim

WORKDIR /app

COPY ./Backend /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]