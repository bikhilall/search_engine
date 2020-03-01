FROM tensorflow/tensorflow:1.15.0-py3

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY dist /usr/src/app/dist
RUN pip3 install ./dist/*

COPY . /usr/src/app

EXPOSE 8080

ENTRYPOINT ["python3"]

CMD ["-m", "api"]