#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

python manage.py migrate --no-input
python manage.py collectstatic --no-input

exec /usr/local/bin/gunicorn config.wsgi --bind 0.0.0.0:1998 --chdir=/app
