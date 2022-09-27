FROM node:12-alpine
# Adding build tools to make yarn install work on Apple silicon / arm64 machines
#RUN apk add --no-cache python2 g++ make
#WORKDIR /app
#COPY . .
#RUN yarn install --production
#CMD ["node", "static/js/app.js"]

# start from base
FROM ubuntu:20.04
WORKDIR /Django-web-app

RUN apt-get -y update && apt-get -y upgrade && apt-get install -y --no-install-recommends \
    python3 libpython3-dev python3-pip python3-dev \
    build-essential libpq-dev nano gcc unixodbc-dev curl gnupg
# default-jre is used to install Java which is used the run Google Closure under Django Compressor
# python3-gdbm is used by Celery to manage its schedule db
# --no-install-recommends is used to only the main dependencies (packages in the Depends field) are installed.

# fetch app specific deps
RUN pip3 freeze > requirements.txt
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# copy our application code
COPY . .

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

# expose port
EXPOSE 8000