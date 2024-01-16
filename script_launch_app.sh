#!/bin/bash

cd /Users/alina/vs-project/project/pipeline_ml

export FLASK_APP=app.py

git pull origin main


pip install -r requirements.txt

# Run the Flask app
nohup flask run --host='0.0.0.0' --port=8081
