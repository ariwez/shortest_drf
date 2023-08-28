SHELL := /bin/bash


# https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-45s\033[0m %s\n", $$1, $$2}'

# helpers
run-app: ## Run application
	docker-compose up web

run-migrate: ## Run migrations
	docker-compose build migrate
	docker-compose run migrate

run-tests: ## Build and run tests in docker
	docker-compose build test
	docker-compose run test

# https://stackoverflow.com/a/63784549
.PHONY: $(shell sed -n -e '/^$$/ { n ; /^[^ .\#][^ ]*:/ { s/:.*$$// ; p ; } ; }' $(MAKEFILE_LIST))
