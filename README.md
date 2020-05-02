# react-flask-starter
A simple starter pack for react and flask development

## Available Scripts

In the project directory, you can run:

### `make setup`

Installs all the nodejs and python(3) requirements for the project

### `make runserver`

Starts the development server with gunicorn

### Heroku deployment steps
```bash
 heroku login
 heroku create
 heroku buildpacks:clear
 heroku buildpacks:add heroku/nodejs
 heroku buildpacks:add heroku/python
 heroku config:set NODE_MODULES_CACHE=false
 git push heroku master

```
