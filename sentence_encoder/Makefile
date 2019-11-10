.PHONY: api/models

api/models:
	docker run --rm -v ${PWD}:/local openapitools/openapi-generator-cli:v4.2.0 generate \
    -i /local/api/openapi/openapi.yaml \
    -g python-flask \
    -c /local/api/config.json \
    -o /local