FROM python:3.8.13

WORKDIR /Workspace

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /Workspace/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /Workspace/requirements.txt

RUN pip install --no-cache-dir --upgrade  Psycopg2

RUN apt-get update && apt-get install -y netcat


COPY . /Workspace/

RUN sed -i 's/\r$//g' /Workspace/entrypoint.sh

RUN chmod +x /Workspace/entrypoint.sh 


ENTRYPOINT [ "/Workspace/entrypoint.sh" ]

