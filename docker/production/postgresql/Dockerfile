FROM postgres:16-bullseye

COPY ./docker/production/postgresql/maintenance /usr/production/bin/maintenance

RUN chmod +x /usr/production/bin/maintenance/*

RUN mv /usr/production/bin/maintenance/* /usr/production/bin \
    && rmdir /usr/production/bin/maintenance
