.PHONY: all html coverage clean

all: html

BUILD_DIR=_build
SPHINXOPTS=-n -W -d $(BUILD_DIR)/doctrees .

html:
	sphinx-build -b html $(SPHINXOPTS) $(BUILD_DIR)/html

coverage:
	sphinx-build -b coverage ${SPHINXOPTS} $(BUILD_DIR)/coverage
	cat build/coverage/python.txt

clean:
	rm -rf ${}BUILD_DIR}
