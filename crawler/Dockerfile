FROM python:3.6.9-slim

RUN mkdir -p /usr/src/crawler
WORKDIR /usr/src/crawler

COPY requirements.txt /usr/src/crawler/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/crawler

ENTRYPOINT ["python3"]

CMD ["main.py"]