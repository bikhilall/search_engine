.PHONY: run

clean:
	cd core && make clean

run:build
	docker-compose up --build

stop:
	docker-compose down

build: build-core

install: install-core

install-core: build-core
	pip3 install --no-cache-dir ./core/dist/*

build-core:
	cd core && make dist
