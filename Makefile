IMAGE_NAME = url_shortener

.PHONY: build run test

build:
	docker build -t $(IMAGE_NAME) .

test: build
	@echo "Running tests..."
	docker run --rm $(IMAGE_NAME) python manage.py test
