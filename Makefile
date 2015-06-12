.PHONY: all test
COVERAGE_DIR = .cover
COVER_PERC = 75
PACKAGE_NAME = prettytable

all: coverage

test:
	@nosetests --with-coverage --cover-package=$(PACKAGE_NAME) --cover-min-percentage=$(COVER_PERC)

clean: clean-pyc clean-build clean-cover

clean-build:
	@rm -rf build
	@rm -rf dist
	@rm -rf *.egg-info

clean-pyc:
	@find . -name '*.pyc' -exec rm {} \;
	@find . -name '__pycache__' -type d | xargs rm -rf

clean-cover:
	@rm -rf $(COVERAGE_DIR)
	@rm -f .coverage

coverage: #clean-cover
	@nosetests --with-coverage --cover-package=$(PACKAGE_NAME) --cover-html --cover-html-dir=$(COVERAGE_DIR)

opencover: coverage
	@open $(COVERAGE_DIR)/index.html

make-docs:
	$(MAKE) -C docs html

develop:
	@pip install -r req-dev.txt

install:
	@python setup.py install

release: test
	@python setup.py register -r pypi
	@python setup.py sdist upload -r pypi

.PHONY: release clean clean-pyc develop install clean-build
.PHONY: coverage clean-cover opencover
