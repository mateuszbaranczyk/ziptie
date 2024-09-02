FROM python:3.10-slim

COPY . .
RUN pip install -r requirements.txt

WORKDIR /app
EXPOSE 8011

ENV PYTHONPATH=/app

CMD ["uvicorn", "app.api:app", "--host=0.0.0.0", "--port=8011"]