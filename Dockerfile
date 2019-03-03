FROM ubuntu:18.04

RUN apt-get update && apt-get install -y python3 python3-dev python3-pip

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

EXPOSE 80

# Click complains otherwise
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

ENV FLASK_APP app

CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]
