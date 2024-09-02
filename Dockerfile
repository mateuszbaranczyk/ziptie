FROM python:3.10-slim

COPY . .
RUN pip install -r requirements.txt

WORKDIR /app
EXPOSE 8011

ENV PYTHONPATH=/app

CMD ["uvicorn", "app.api:app", "--port=8011"]