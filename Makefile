PYTHON ?= python3
VENV ?= .venv

.PHONY: setup train lint format

setup:
	$(PYTHON) -m venv $(VENV)
	. $(VENV)/bin/activate && pip install --upgrade pip && pip install -r requirements.txt

train:
	@if [ -z "$$TRAIN_DATA_PATH" ]; then echo "Set TRAIN_DATA_PATH first"; exit 1; fi
	$(PYTHON) VertexAI_model_train/task.py --data-path $$TRAIN_DATA_PATH

lint:
	@echo "Add linter configuration when codebase grows (e.g., ruff)."

format:
	@echo "Add formatter configuration when codebase grows (e.g., black)."
