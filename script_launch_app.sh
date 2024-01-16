cd /Users/alina/vs-project/project/pipeline_ml

git pull origin main

pip install -r requirements.txt

flask run --host='0.0.0.0' --port=8081
