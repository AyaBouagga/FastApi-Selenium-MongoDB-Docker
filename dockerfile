FROM python:3.8.10

WORKDIR /usr/scr/application

COPY requirements.txt ./

RUN pip3 install --no-cache-dir --upgrade -r ./requirements.txt

COPY . . 


