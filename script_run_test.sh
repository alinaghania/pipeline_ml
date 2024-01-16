#!/bin/bash

BRANCH_NAME=$1

cd /Users/alina/vs-project/project/pipeline_ml

git pull origin $BRANCH_NAME

pip install -r requirements.txt

pytest 