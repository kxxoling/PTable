.PHONY: all test
COVERAGE_DIR = .cover
COVER_PERC = 75
PACKAGE_NAME = prettytable

.PHONY: all
all: coverage

.PHONY: test
test:
	@nosetests --with-coverage --cover-package=$(PACKAGE_NAME) --cover-min-percentage=$(COVER_PERC)

.PHONY: clean
clean: clean-pyc clean-build clean-cover

.PHONY: clean-build
clean-build:
	@rm -rf build
	@rm -rf dist
	@rm -rf *.egg-info

.PHONY: clean-pyc
clean-pyc:
	@find . -name '*.pyc' -exec rm {} \;
	@find . -name '__pycache__' -type d | xargs rm -rf

.PHONY: clean-cover
clean-cover:
	@rm -rf $(COVERAGE_DIR)
	@rm -f .coverage

.PHONY: coverage
coverage: #clean-cover
	@nosetests --cover-erase --with-coverage --cover-package=$(PACKAGE_NAME) --cover-html --cover-html-dir=$(COVERAGE_DIR)

.PHONY: opencover
opencover: coverage
	@open $(COVERAGE_DIR)/index.html

.PHONY: make-docs
make-docs:
	$(MAKE) -C docs html

.PHONY: develop
develop:
	@pip install -r req-dev.txt

.PHONY: install
install:
	@python setup.py install

.PHONY: release
release: test
	@python setup.py register -r pypi
	@python setup.py sdist upload -r pypi


