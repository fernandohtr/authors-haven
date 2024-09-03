ARG PYTHON_VERSION=3.12.4-bullseye

FROM python:${PYTHON_VERSION} AS python

FROM python AS python-build-stage
ARG BUILD_ENVIRONMENT=production

RUN apt update && apt install --no-install-recommends -y \
    build-essential \
    libpq-dev

COPY ./requirements .

RUN pip wheel --wheel-dir /usr/src/app/wheels \
    -r ${BUILD_ENVIRONMENT}.txt

FROM python AS python-run-stage
ARG BUILD_ENVIRONMENT=production

ARG APP_HOME=/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV BUILD_ENV ${BUILD_ENVIRONMENT}

WORKDIR ${APP_HOME}

RUN addgroup --system django && \
    adduser --system --ingroup django django && \
    mkdir -p ${APP_HOME}/staticfiles && \
    chown django:django ${APP_HOME}/staticfiles && \
    chmod 775 ${APP_HOME}/staticfiles

RUN apt-get update && apt-get install --no-install-recommends -y \
    libpq-dev \
    gettext \
    netcat \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

COPY --from=python-build-stage /usr/src/app/wheels /wheels

RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
    && rm -rf /wheels/

COPY --chown=django:django ./docker/production/django/entrypoint.sh /entrypoint.sh
RUN sed -i "s/\r$//g" /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY --chown=django:django ./docker/production/django/start.sh /start.sh
RUN sed -i "s/\r$//g" /start.sh
RUN chmod +x /start.sh

COPY --chown=django:django ./docker/production/django/celery/worker/start-celery-worker.sh /start-celery-worker.sh
RUN sed -i "s/\r$//g" /start-celery-worker.sh
RUN chmod +x /start-celery-worker.sh

COPY ./docker/production/django/celery/flower/start-flower.sh /start-flower.sh
RUN sed -i "s/\r$//g" /start-flower.sh
RUN chmod +x /start-flower.sh

COPY --chown=django:django ./src ${APP_HOME}

RUN chown django:django ${APP_HOME}

USER django

ENTRYPOINT ["/entrypoint.sh"]
