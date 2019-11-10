.PHONY: api/models

api/models:
	docker run --rm -v ${PWD}:/local \
	swaggerapi/swagger-codegen-cli-v3:3.0.13 generate \
	-i /local/api/swagger/swagger.yaml \
	-l python-flask \
	-o /local/ \
	--config /local/api/config.json \
	-Dmodels