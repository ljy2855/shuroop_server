FROM python:3.8.13

RUN mkdir -p /home/app

ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME

WORKDIR $APP_HOME

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt $APP_HOME/requirements.txt

RUN pip install --no-cache-dir --upgrade -r $APP_HOME/requirements.txt

RUN pip install --no-cache-dir --upgrade  Psycopg2

RUN apt-get update && apt-get install -y netcat


COPY . $APP_HOME

RUN sed -i 's/\r$//g' $APP_HOME/entrypoint.sh

RUN chmod +x $APP_HOME/entrypoint.sh 



ENTRYPOINT [ "/home/app/web/entrypoint.sh" ]

