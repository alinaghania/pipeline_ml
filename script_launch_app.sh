#!/bin/bash

# Configuration
REPO_DIR="/Users/alina/vs-project/project/pipeline_ml"
LOG_DIR="${REPO_DIR}/logs"
STDOUT_LOG="${LOG_DIR}/stdout.log"
STDERR_LOG="${LOG_DIR}/stderr.log"
FLASK_APP_PATH="${REPO_DIR}/app.py"

# Créer le répertoire de logs si nécessaire
mkdir -p "${LOG_DIR}"

# Se déplacer dans le répertoire du dépôt
cd "${REPO_DIR}"

# Configurer Git pour éviter les problèmes de branches divergentes
git config pull.rebase false

# Mettre à jour le code source
git pull origin main

# Mettre à jour pip et installer les dépendances
pip install --upgrade pip
pip install -r requirements.txt

# Définir le chemin vers l'application Flask
export FLASK_APP="${FLASK_APP_PATH}"

# Démarrer l'application Flask en arrière-plan
nohup flask run --host=0.0.0.0 --port=8081 > "${STDOUT_LOG}" 2> "${STDERR_LOG}" &

# Message de confirmation
echo "Application Flask lancée et logs enregistrés dans ${LOG_DIR}"
