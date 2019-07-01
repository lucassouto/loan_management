clean: clean-build clean-pyc clean-test

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -fr .tox/
	rm -f .coverage
	rm -f .coverage.xml
	rm -fr htmlcov/
	rm -fr .mypy_cache/
	rm -fr .pytest_cache/

createsuperuser:
	docker-compose -f local.yml run --rm app python manage.py createsuperuser

up-local:
	docker-compose -f local.yml up -d --build
	docker-compose -f local.yml logs -f

down-local:
	docker-compose -f local.yml down -v
	docker-compose -f local.yml rm -f

build-prd:
	docker-compose -f production.yml up -d --build

tests: clean
	docker-compose -f local.yml up -d --build
	docker-compose -f local.yml run --rm app pytest --cov
