

local:
	poetry export -f requirements.txt --without-hashes --without-urls -o requirements/local.txt

prod:
	poetry export -f requirements.txt --without-hashes --without-urls -o requirements/production.txt

lint:
	ruff check . && ruff check . --diff

format:
	ruff check . --fix && ruff format .

build:
	docker compose -f local.yml up -d --build --remove-orphans

up:
	docker compose -f local.yml up -d

stop:
	docker compose -f local.yml stop

down:
	docker compose -f local.yml down

logs:
	docker compose -f local.yml logs -f

backup:
	docker compose -f local.yml exec postgres backup.sh

list-backup:
	docker compose -f local.yml exec postgres backups.sh

restore-backup:
	docker compose -f local.yml exec postgres restore.sh $(BACKUP_FILE)
