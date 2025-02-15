export COMPOSE_DOCKER_CLI_BUILD=1
export DOCKER_BUILDKIT=1
export COMPOSE_IGNORE_ORPHANS=1
export COMPOSE_BAKE=true


pull:
	docker compose -f postgres.yml pull
build:
	docker compose -f articles_platform.yml -f postgres.yml build
up: build
	docker compose -f postgres.yml -f articles_platform.yml up -d
down:
	docker compose -f articles_platform.yml -f postgres.yml down
