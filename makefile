install:
	@poetry install

py-organizer:
	@poetry run py-organizer

build:
	@poetry build

package-install:
	@pip install --user dist/*.whl

lint:
	@poetry run flake8 py_organizer

test:
	@poetry run pytest

test-coverage-report:
	@poetry run pytest --cov=py-organizer --cov-report xml

test-coverage:
	@poetry run pytest --cov=py-organizer