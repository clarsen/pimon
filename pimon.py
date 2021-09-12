import os
import socket
import time

import influxdb_client
import vcgencmd


def record(client, vcgm):
    global hostname
    global client_write
    temp_c = vcgm.measure_temp()

    json_body = [
        {
            "measurement": "temperature_c",
            "tags": {
                "host": hostname,
            },
            "fields": {
                "value": float(temp_c),
            },
        }
    ]
    try:
        # sometimes network requests fail, but don't fail this loop
        client_write.write(bucket=os.environ.get("INFLUXDB_BUCKET"), record=json_body)
    except Exception as e:
        print(e)


def loop(client, vcgm):
    while True:
        record(client, vcgm)
        time.sleep(15)


def main():
    global hostname
    global client_write
    client = influxdb_client.InfluxDBClient(
        url=os.environ.get("INFLUXDB_URL"),
        token=os.environ.get("INFLUXDB_TOKEN"),
        org=os.environ.get("INFLUXDB_ORG"),
    )
    client_write = client.write_api(
        write_options=influxdb_client.client.write_api.SYNCHRONOUS
    )
    hostname = os.environ.get("HOST")
    print(hostname)
    vcgm = vcgencmd.Vcgencmd()

    loop(client, vcgm)


if __name__ == "__main__":
    main()
