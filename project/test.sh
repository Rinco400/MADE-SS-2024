#!/bin/bash

# Check if Python 3 is installed
if ! command -v python3 >/dev/null 2>&1 
then
    echo "The data pipeline needs Python 3 to run, but it is not installed."
    echo "Install Python 3 e.g. via apt (sudo apt install python3)."
    echo "Aborting..."
    exit 1
fi

# Install required packages
python3 -m pip install -r ./project/requirements.txt

# Start the data pipeline script
echo "Starting data pipeline script"
echo
python3 ./project/pipeline.py

# Absolute path to the SQLite database
DB_PATH=$(realpath ../data/cleaned_data.db)
echo "Checking SQLite DB Path: $DB_PATH"

# Check if the SQLite database was created
if [ ! -f "$DB_PATH" ]; then
    echo "SQLite database wasn't found. Seems like the data pipeline ran into an error..."
    exit 1
fi

# Start the test script
echo "Starting test script"
echo
python3 ./project/test.py

# Check the exit status of the test script
if [ $? -ne 0 ]; then
    echo "Some tests failed."
    exit 1
fi

echo
echo "All tests for the data pipeline passed."


