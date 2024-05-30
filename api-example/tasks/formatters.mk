format-sources: ## Format the project sources.
	poetry run ruff format src/api_example/ tests/

formatters: format-sources ## Run all the formatters.