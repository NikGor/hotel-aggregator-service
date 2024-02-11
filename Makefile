.PHONY: install test lint run clean add-and-commit build migrate

install:
	poetry install

test:
	poetry run python manage.py test

lint:
	poetry run flake8

run:
	poetry run python manage.py runserver

clean:
	find . -name "*.pyc" -delete

amend-and-push:
	git add .
	git commit --amend --no-edit
	git push --force

build:
	docker build -t django-app .

migrate:
	poetry run python manage.py makemigrations
	poetry run python manage.py migrate
