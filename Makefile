PYTHON ?= python

.PHONY: data test inventory train

data:
	$(PYTHON) -m climateshield make-data

inventory:
	$(PYTHON) -m climateshield inventory

test:
	$(PYTHON) -m pytest tests -q

train:
	$(PYTHON) -m climateshield train
