FROM python:3.13-alpine

WORKDIR /sge

# Impede criação de .pyc
ENV PYTHONDONTWRITEBYTECODE=1
# Mostra logs na hora
ENV PYTHONUNBUFFERED=1

COPY . .

RUN apk add --no-cache postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
