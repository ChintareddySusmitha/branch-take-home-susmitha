FROM python:3.10.4-slim-buster

# Update and install system packages
RUN apt-get update -y && \
  apt-get install --no-install-recommends -y -q \
  git libpq-dev python-dev && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

#Keeps Python from generating .pyc files
ENV PYTHONDONTWRITEBYTECODE 1

#Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

ADD requirements.txt .
RUN python -m pip install -r requirements.txt

EXPOSE 9200

# Set working directory
WORKDIR /python