.PHONY: api/models

api/models:
	docker run --rm -v "${shell pwd}":"/local" \
	swaggerapi/swagger-codegen-cli-v3:3.0.13 generate \
	-l python-flask \
	-i /local/api/swagger/swagger.yaml \
	-o /local/ \
	--config /local/api/config.json \
	-Dmodels