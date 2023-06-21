init:
	pip install -r requirements.txt

test:
	python -m pytest tests --capture=no

format:
	python -m black confclient/*