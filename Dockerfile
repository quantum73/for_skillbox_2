FROM python:3.8.6-alpine
ENV PYTHONUNBUFFERED=1
RUN apk update && apk add postgresql-dev postgresql-client gcc python3-dev musl-dev
RUN pip install --upgrade pip
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
RUN chmod +x /code/wait-for-postgres.sh