FROM python:3-alpine

RUN apk add raspberrypi

WORKDIR /app
COPY requirements.txt /app
RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install vcgencmd influxdb_client

COPY pimon.py /app/
COPY entrypoint.sh /entrypoint.sh
RUN chmod 555 /entrypoint.sh


ENV INFLUXDB_URL "MUST SET"
ENV INFLUXDB_TOKEN "MUST SET"
ENV INFLUXDB_ORG "MUST SET"
ENV INFLUXDB_BUCKET "infra"

ENV HOST MUST_SET

ENTRYPOINT [ "/entrypoint.sh" ]
CMD [ "python3", "-u", "/app/pimon.py" ]
