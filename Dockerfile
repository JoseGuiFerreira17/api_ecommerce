FROM python:3.11-buster

ARG REQUIREMENTS_PATH=requirements.txt

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV APP_HOME=/home/app

RUN mkdir $APP_HOME
WORKDIR $APP_HOME

COPY . $APP_HOME

RUN apt update && apt install -y netcat

RUN pip install --upgrade --no-cache pip
RUN pip install --no-cache-dir -r $APP_HOME/$REQUIREMENTS_PATH

COPY ./entrypoint.sh .
RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["/home/app/entrypoint.sh"]
