.PHONY: run

clean:
	cd search_engine_core && make clean

run:build
	docker-compose up --build

stop:
	docker-compose down

build: build-core

install: install-core

install-core: build-core
	pip3 install --no-cache-dir ./search_engine_core/dist/*

build-core:
	cd search_engine_core && make dist
