UVICORN		:= ../.venv/bin/uvicorn
PYTHON		:= ../.venv/bin/python3
PIP			:= ../.venv/bin/pip3

ch check_health: ### Check if all required binaries are available and executable
	@echo "Checking if UVICORN, PYTHON3 and PIP3 exist and are executable..."
	@if [ ! -x $(UVICORN) ]; then\
		echo "[!] Error: UVICORN is missing or not executable";\
		exit 1;\
	fi
	@if [ ! -x $(PYTHON) ]; then\
		echo "[!] Error: PYTHON3 is missing or not executable";\
		exit 1;\
	fi
	@if [ ! -x $(PIP) ]; then\
		echo "[!] Error: PIP3 is missing or not executable";\
		exit 1;\
	fi
	@echo "All binaries are available and executable\n"

.PHONY: ch check_health

dev: check_health ### Run the development server
	$(UVICORN) src.main:app --reload

.PHONY: dev

up run: check_health ### Run the production server
	$(UVICORN) src.main:app

.PHONY: up run

## TODO \/\/\/\/
## install: check_health ### Install all required dependencies
##	$(PIP) install -r requirements.txt

h help: ### Display this help message
	@echo "Available targets:"
	@awk 'BEGIN {FS = ":.*?###"} /^[a-zA-Z0-9_-_ ]+:.*?###/ {printf "\033[34m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.PHONY: h help
