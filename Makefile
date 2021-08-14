SHELL=/bin/bash

setup: requirements.txt
	test -d .venv || python3 -m venv .venv
	. .venv/bin/activate; pip install -U pip; pip install -r requirements.txt

include .env
export
run: .venv
	. .venv/bin/activate; FLASK_APP=main FLASK_ENV=development flask run

add_dep: .venv
	. .venv/bin/activate; pip install $(dep) && pip freeze | grep -v "pkg-resources" > requirements.txt

rm_dep: .venv
	. .venv/bin/activate; pip uninstall -y $(dep) && pip freeze | grep -v "pkg-resources" > requirements.txt

include .env
export
runcommand: .venv
	. .venv/bin/activate; FLASK_APP=app/scripts FLASK_ENV=development flask $(command)
