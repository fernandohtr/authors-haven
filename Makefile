

local:
	poetry export -f requirements.txt --with dev --without-hashes --without-urls -o requirements/local.txt

prod:
	poetry export -f requirements.txt --without-hashes --without-urls -o requirements/production.txt

lint:
	@docker compose -f local.yml exec api ruff check . && ruff check . --diff

format:
	@docker compose -f local.yml exec api ruff check . --fix && ruff format .

build:
	docker compose -f local.yml up -d --build --remove-orphans

up:
	docker compose -f local.yml up -d

stop:
	docker compose -f local.yml stop

down:
	docker compose -f local.yml down

logs:
	@docker compose -f local.yml logs -f

logs-api:
	@docker compose -f local.yml logs -f api

makemigrations:
	docker compose -f local.yml run --rm api python src/manage.py makemigrations

migrate:
	docker compose -f local.yml run --rm api python src/manage.py migrate

collectstatic:
	docker compose -f local.yml run --rm api python src/manage.py collectstatic --no-input --clear

superuser:
	docker compose -f local.yml run --rm api python src/manage.py createsuperuser

db:
	docker compose -f local.yml exec postgres psql --username=fernando --dbname=authors-live

down-volumes:
	docker compose -f local.yml down -v

volume:
	docker volume inspect authors-haven_local_postgres_data

backup:
	docker compose -f local.yml exec postgres backup.sh

list-backup:
	docker compose -f local.yml exec postgres backups.sh

restore-backup:
	docker compose -f local.yml exec postgres restore.sh $(BACKUP_FILE)
