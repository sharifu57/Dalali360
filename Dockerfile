FROM python:3.8.5
LABEL Name=dalali Version=1.0
FROM python:3

RUN mkdir /dalali
WORKDIR /dalali
ADD requirements.txt /dalali/
RUN pip install -r requirements.txt
EXPOSE 7000

