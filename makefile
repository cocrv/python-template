.PHONY: init test

init:
	virtualenv -p /usr/bin/python3.7 venv && \
	pip install -r requirements.txt 

test:
	py.test --verbose tests 
	pytest --cov=calculator --cov-fail-under=100 tests/

