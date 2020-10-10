#!/bin/sh
set -eu

PATH=/opt/vc/bin:$PATH
export PATH


exec "$@"
