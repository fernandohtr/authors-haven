DOCKER_LOCAL:=docker compose -f local.yml

local:
	poetry export -f requirements.txt --with dev --without-hashes --without-urls -o requirements/local.txt

prod:
	poetry export -f requirements.txt --without-hashes --without-urls -o requirements/production.txt

lint:
	@${DOCKER_LOCAL} exec api sh -c "ruff check . && ruff check . --diff"

format:
	@${DOCKER_LOCAL} exec api sh -c "ruff check . --fix && ruff format ."

build:
	${DOCKER_LOCAL} up -d --build --remove-orphans

up:
	${DOCKER_LOCAL} up -d

stop:
	${DOCKER_LOCAL} stop

down:
	${DOCKER_LOCAL} down

logs:
	@${DOCKER_LOCAL} logs -f

logs-api:
	@${DOCKER_LOCAL} logs -f api

makemigrations:
	${DOCKER_LOCAL} run --rm api python src/manage.py makemigrations

migrate:
	${DOCKER_LOCAL} run --rm api python src/manage.py migrate

collectstatic:
	${DOCKER_LOCAL} run --rm api python src/manage.py collectstatic --no-input --clear

superuser:
	${DOCKER_LOCAL} run --rm api python src/manage.py createsuperuser

db:
	${DOCKER_LOCAL} exec postgres psql --username=fernando --dbname=authors-live

down-volumes:
	${DOCKER_LOCAL} down -v

volume:
	docker volume inspect authors-haven_local_postgres_data

backup:
	${DOCKER_LOCAL} exec postgres backup.sh

list-backup:
	${DOCKER_LOCAL} exec postgres backups.sh

restore-backup:
	${DOCKER_LOCAL} exec postgres restore.sh $(BACKUP_FILE)

create-index:
	${DOCKER_LOCAL} exec api python src/manage.py search_index --create 

populate-index:
	${DOCKER_LOCAL} exec api python src/manage.py search_index --populate
