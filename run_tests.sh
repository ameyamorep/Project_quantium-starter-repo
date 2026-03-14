#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Activate the virtual environment
echo "Activating virtual environment..."
source pyvenv/Scripts/activate

# Run the test suite
echo "Running tests..."
if pytest test_dash_app.py -v; then
    echo "All tests passed!"
    exit 0
else
    echo "Tests failed!"
    exit 1
fi
