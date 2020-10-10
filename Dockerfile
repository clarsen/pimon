FROM python:3-alpine

RUN apk add raspberrypi
RUN pip3 install vcgencmd influxdb

COPY pimon.py /app/
COPY entrypoint.sh /app/
RUN chmod 555 /app/entrypoint.sh

ENV INFLUX_HOST MUST_SET
ENV INFLUX_DB infra
ENV INFLUX_HOST_VERIFY_CERT 1
ENV INFLUX_USER infra-rw
ENV INFLUX_PASSWORD MUST_SET
ENV HOST MUST_SET

WORKDIR /app
ENTRYPOINT [ "./entrypoint.sh" ]
CMD [ "python3", "-u", "./pimon.py" ]
