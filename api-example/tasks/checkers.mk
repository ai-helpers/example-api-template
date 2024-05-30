check-types: ## Check the project code types with mypy.
	poetry run mypy src/api_example/ tests/ --config-file .mypy.ini

check-tests: ## Check the project unit tests with pytest.
	poetry run pytest --numprocesses="auto" tests/

check-format: ## Check the project source format with ruff.
	poetry run ruff format --check src/api_example/ tests/

check-poetry: ## Check the project pyproject.toml with poetry.
	poetry check --lock

check-quality: ## Check the project code quality with ruff.
	poetry run ruff check src/api_example/ tests/

check-security: ## Check the project code security with bandit.
	poetry run bandit --recursive --configfile=pyproject.toml src/api_example/

check-coverage: ## Check the project test coverage with coverage.
	poetry run pytest --cov=src/api_example/ --cov-fail-under=80 --numprocesses="auto" tests/

checkers: check-types check-format check-quality check-security check-coverage ## Run all the checkers.