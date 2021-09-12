#!/bin/sh
set -eEu

docker build --rm -t clarsen7/pimon .
docker push clarsen7/pimon
