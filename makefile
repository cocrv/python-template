.PHONY: init test

init:
	virtualenv -p /usr/bin/python3.7 venv

install:
	pip install -r requirements.txt 

test:
	pytest --verbose tests 
	pytest --cov=src --cov-fail-under=100 tests/

