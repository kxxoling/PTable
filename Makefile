.PHONY: all test

all: test

test:

clean: clean-pyc clean-build

clean-build:
	@rm -rf build
	@rm -rf dist
	@rm -rf *.egg-info

clean-pyc:
	@find . -name '*.pyc' -exec rm {} \;
	@find . -name '__pycache__' -type d | xargs rm -rf

make-docs:
	$(MAKE) -C docs html

develop:
	@pip install --editable .

install:
	@python setup.py install

release: test
	@python setup.py register -r pypi
	@python setup.py sdist upload -r pypi

.PHONY: release clean clean-pyc develop install clean-build
