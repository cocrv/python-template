.PHONY: init test

init:
	pip install -r requirements.txt

test:
	py.test --verbose tests
	pytest --cov=calculator tests/

