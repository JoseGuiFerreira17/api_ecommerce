prebuild:
	cp example.env .env
	cp example.db.env .db.env

migrate:
	docker compose exec ecommerce_django python manage.py migrate

makemigrations:
	docker compose exec ecommerce_django python manage.py makemigrations

reset_migrations:
	docker compose exec ecommerce_django find . -path "*/migrations/*.py" -not -name "__init__.py" -not -path "*/venv/*" -delete
	docker compose exec ecommerce_django python manage.py makemigrations

delete_pycache:
	find . -path "*/__pycache__" | xargs rm -rf

test:
	python manage.py test

lint:
	black .
	flake8 . --extend-exclude=migrations,venv --max-line-length 120

runserver:
	docker compose up
