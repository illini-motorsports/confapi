init:
	pip install -r requirements.txt

test:
	python -m pytest tests

testcov:
	python -m pytest --cov=confclient --cov-report=html tests

format:
	python -m black confclient/*