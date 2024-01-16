#!/bin/bash

# Enable verbose mode
set -x

# Redirect stderr to a log file
exec 2>error_log.txt

# Change to the directory of the script
cd "$(dirname "$0")"

# Set the FLASK_APP environment variable
export FLASK_APP=app.py

# Pull the latest changes from the main branch
git pull origin main

# Install required Python packages
pip install -r requirements.txt

# Run the Flask app
flask run --host='0.0.0.0' --port=8081
