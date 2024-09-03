#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

worker_ready() {
    celery -A config.celery inspect ping
}

until worker_ready; do
    >&2 echo "Celery workers not available :-("
    sleep 1
done

>&2 echo "Celery workers are available and ready!... :-)"

exec watchfiles celery.__main__.main \
    --args \
    "-A config.celery -b '${CELERY_BROKER}' flower --basic_auth=${CELERY_FLOWER_USER}:${CELERY_FLOWER_PASSWORD} --broker_api=${CELERY_BROKER_API}"

