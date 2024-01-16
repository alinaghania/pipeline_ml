#!/bin/bash

cd /Users/alina/vs-project/project/pipeline_ml

git pull origin main

pip install -r requirements.txt

pytest 