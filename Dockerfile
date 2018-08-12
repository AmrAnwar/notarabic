FROM python:3
ENV PYTHONUNBUFFERED 1
#ENV C_FORCE_ROOT true
#RUN apt-get update && apt-get install
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/