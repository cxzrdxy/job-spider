FROM mcr.microsoft.com/playwright/python:v1.51.0-jammy
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY backend /app/backend
ENV PYTHONUNBUFFERED=1
WORKDIR /app/backend
CMD ["python","manage.py","runserver","0.0.0.0:8000"]
