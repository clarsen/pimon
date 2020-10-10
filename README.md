# Requirements

```
python3 -m venv .env
. .env/bin/activate
pip3 install vcgencmd influxdb
sudo apt-get install entr
```

# dev test
```
INFLUX_HOST=<hostname-of-influxdb> \
INFLUX_DB=<influx database> \
INFLUX_USER=<influx-user> \
INFLUX_PASSWORD=<password-of-influx-user> \
INFLUX_HOST_VERIFY_CERT=1 \
python3 pimon.py
```

# build container
```
docker build -t clarsen7/pimon .
docker push clarsen7/pimon
```

# Start container
```
docker run --name pimon \
  -d \
  --restart unless-stopped \
  -e HOST=`hostname` \
  --device /dev/vchiq \
  -e INFLUX_HOST=<hostname-of-influxdb> \
  -e INFLUX_PASSWORD=<password-of-influx-user> \
  clarsen7/pimon
```
