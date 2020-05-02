VENV := .virtualenv

runserver:
	. $(VENV)/bin/activate \
	&& gunicorn --workers=1 --access-logfile - --bind=0.0.0.0:8000 --log-level=debug server:app  