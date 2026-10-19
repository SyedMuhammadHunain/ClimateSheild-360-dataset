PYTHON ?= python

.PHONY: data test inventory

data:
	$(PYTHON) -m climateshield make-data

inventory:
	$(PYTHON) -m climateshield inventory

test:
	$(PYTHON) -m pytest tests -q
