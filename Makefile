local:
	poetry export -f requirements.txt --without-hashes --without-urls -o requirements/local.txt

prod:
	poetry export -f requirements.txt --without-hashes --without-urls -o requirements/production.txt

lint:
	ruff check . && ruff check . --diff

format:
	ruff check . --fix && ruff format .