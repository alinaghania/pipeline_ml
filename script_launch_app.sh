#!/bin/bash

# Enable verbose mode
set -x

# Redirect stderr to a log file
exec 2>error_log.txt

# Change to the directory of the script
cd "$(dirname "$0")"

# Set the FLASK_APP environment variable
export FLASK_APP=app.py

# Set a git pull strategy to avoid the need for user input on divergent branches
git config pull.rebase false

# Pull the latest changes from the main branch
# This command will exit with non-zero if there are merge conflicts
git pull origin main

# If git pull fails, exit the script with an error code
if [ $? -ne 0 ]; then
    echo "Git pull failed, exiting..."
    exit 1
fi

# Install required Python packages
pip install -r requirements.txt

# Check if Flask is installed, exit if not
if ! command -v flask &> /dev/null; then
    echo "Flask is not installed, exiting..."
    exit 1
fi

# Run the Flask app
flask run --host='0.0.0.0' --port=8081
