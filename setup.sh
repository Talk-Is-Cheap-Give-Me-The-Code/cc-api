#!/bin/sh

# Check if python3 is installed
if ! command -v python3 2>&1 > /dev/null
then
	echo "Python3 is not installed. Please install python3."
	exit 1
fi

# Activate the virtual environment
if [ -d .venv ]
then
	echo "Virtual environment already exists."
else
	echo "Creating virtual environment..."
	python3 -m venv .venv
fi

# Install the required packages
. .venv/bin/activate
pip install -r requirements/base.txt

echo "\n\nRun 'source .venv/bin/activate' to activate the virtual environment."