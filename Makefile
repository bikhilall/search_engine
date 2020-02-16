.PHONY: run

clean:
	cd core && make clean

run:build
	docker-compose up --build

stop:
	docker-compose down

build-core:
	cd core && make dist

build: build-core