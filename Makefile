SHELL=/bin/bash

all: install unittest

install:
	pip install .[dev]

unittest: test-parser test-exec test-search

test-%:
	pytest "test/test_`echo $@ | awk -F '-' '{print $$2}'`.py"

