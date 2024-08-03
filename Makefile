local:
	poetry export -f requirements.txt --without-hashes --without-urls -o requirements/local.txt

prod:
	poetry export -f requirements.txt --without-hashes --without-urls -o requirements/production.txt
