.PHONY: run

clean:
	cd core && make clean
	cd crawler && make clean

run:build
	docker-compose up --build

stop:
	docker-compose down

build: build-core build-crawler

build-core:
	cd core && make dist

build-crawler:
	cd crawler && make build

install: install-core

install-core: build-core
	pip3 install ./core/dist/*