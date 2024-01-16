#!/bin/bash

# Active le mode débogage pour afficher toutes les commandes
set -x

# Redirige stdout et stderr dans des fichiers de log séparés
LOG_DIR="/Users/alina/vs-project/project/pipeline_ml"
mkdir -p "$LOG_DIR"
STDOUT_LOG="$LOG_DIR/stdout.log"
STDERR_LOG="$LOG_DIR/stderr.log"

exec 1>>"$STDOUT_LOG"
exec 2>>"$STDERR_LOG"

# Affiche la date et l'heure actuelles
echo "Starting script at $(date)"

# Vérifie l'utilisateur actuel
echo "Running as user: $(whoami)"

# Vérifie le répertoire de travail
echo "Working directory: $(pwd)"

# Définit le chemin absolu vers l'environnement Python et les scripts
REPO_DIR="/Users/alina/vs-project/project/pipeline_ml"
SCRIPT_DIR="$REPO_DIR/scripts"
FLASK_APP_PATH="$REPO_DIR/app.py"
REQUIREMENTS_PATH="$REPO_DIR/requirements.txt"

# Active l'environnement virtuel Python si nécessaire
# source /path/to/your/venv/bin/activate

# Se déplace dans le répertoire du dépôt Git
cd "$REPO_DIR" || { echo "Failed to enter directory $REPO_DIR"; exit 1; }

# Tentative de pull de Git avec configuration pour éviter les messages de divergence
git config pull.rebase false
git pull origin main || { echo "Git pull failed, exiting..."; exit 1; }

# Installe les dépendances
pip install --upgrade pip
pip install -r "$REQUIREMENTS_PATH" || { echo "Pip install failed, exiting..."; exit 1; }

# Lance l'application Flask
export FLASK_APP="$FLASK_APP_PATH"
flask run --host='0.0.0.0' --port=8081
