#!/usr/bin/bash
set -eEuo pipefail
cd $(dirname $0)
. .env/bin/activate
exec python3 pimon.py
