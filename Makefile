VENV := .virtualenv

virtualenv:
	python3 -m venv --clear --prompt='react-flask' $(VENV)
	source $(VENV)/bin/activate && pip install --upgrade pip pip-tools && \
	pip-sync requirements.txt

setup: virtualenv
	npm install	\
	&& npm run build

clean:
	rm -rf build
	rm -rf $(VENV)
	rm -rf node_modules

runserver:
	. $(VENV)/bin/activate \
	&& gunicorn --workers=1 --access-logfile - --bind=0.0.0.0:8000 --log-level=debug server:app  