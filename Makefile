run:
	python src/main.py

test:
	pytest

docker-build:
	docker build -t hello_world_app_python .

docker-run:
	docker-compose up --build
