import os
import socket
import time

import influxdb
import vcgencmd


def record(client, vcgm):
    global hostname
    temp_c = vcgm.measure_temp()

    json_body = []
    json_body.append(
        {
            "measurement": "temperature_c",
            "tags": {
                "host": hostname,
            },
            "fields": {
                "value": float(temp_c),
            },
        }
    )
    try:
        # sometimes network requests fail, but don't fail this loop
        client.write_points(json_body)
    except Exception as e:
        print(e)
        pass


def loop(client, vcgm):
    while True:
        record(client, vcgm)
        time.sleep(15)


def main():
    global hostname
    client = influxdb.InfluxDBClient(
        host=os.environ.get("INFLUX_HOST"),
        port=8086,
        timeout=10,
        database=os.environ.get("INFLUX_DB"),
        ssl=True,
        verify_ssl=False,  # os.environ.get("INFLUX_HOST_VERIFY_CERT"),
        username=os.environ.get("INFLUX_USER"),
        password=os.environ.get("INFLUX_PASSWORD"),
    )
    hostname = os.environ.get("HOST")
    print(hostname)
    vcgm = vcgencmd.Vcgencmd()

    loop(client, vcgm)


if __name__ == "__main__":
    main()
