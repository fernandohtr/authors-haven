#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

python src/manage.py migrate --no-input
python src/manage.py collectstatic --no-input

exec python src/manage.py runserver 0.0.0.0:8000
