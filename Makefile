#
# Makefile
#

clean_pyc:
	find . -name \*.pyc -delete

install:
	bash -c 'pip install -e .'

develop:
	bash -c 'pip install -e .[develop]'

test:
	python setup.py nosetests

build-docs:
	make -C docs clean
	make -C docs html

view-docs: build-docs
	open docs/_build/html/index.html
