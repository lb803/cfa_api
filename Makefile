DOCKER-TAG = lb803/cfa_api
DOCKER-PORTS = -p 8000:8000

.PHONY: build test run

build:
	docker build . -f Dockerfile -t $(DOCKER-TAG)

test:
	docker run --rm $(DOCKER-TAG) -m pytest tests/

run:
	docker run --rm $(DOCKER-PORTS) $(DOCKER-TAG) -m fastapi run cfa_api/main.py
