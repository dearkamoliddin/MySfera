FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY requirements.txt requirements.txt
COPY requirements.txt requirements.txt

#RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["gunicorn", "--bind", "0.0.0.0:8008", "myproject.wsgi:application"]
