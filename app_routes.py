from flask import Blueprint, jsonify, request
import os
import subprocess

deployment_blueprint = Blueprint('deployment', __name__)
testing_blueprint = Blueprint('testing', __name__)

@testing_blueprint.route("/", methods=['POST'])
def testing():
    # Extract the JSON payload
    payload = request.get_json()
    print(f"Received payload: {payload}")  # Log the received payload

    # Extract the branch name from the payload
    branch_name = payload.get('ref', '')
    print(f"Extracted branch name: {branch_name}")  # Log the extracted branch name

    if branch_name == 'refs/heads/staging':
        os.system('git pull origin staging')
        return jsonify({'success': True}), 200, {'ContentType': 'application/json'}
    
    return jsonify({'success': False}), 400, {'ContentType': 'application/json'} 

@deployment_blueprint.route("/", methods=['POST'])
def deployment():
    # Extract the JSON payload
    payload = request.get_json()
    print(f"Received payload: {payload}")  # Log the received payload

    # Extract the branch name from the payload
    branch_name = payload.get('ref', '')
    print(f"Extracted branch name: {branch_name}")  # Log the extracted branch name

    if branch_name == 'refs/heads/main':
        try:
            subprocess.check_output(['git', 'pull', 'origin', 'main'])
            return jsonify({'success': True}), 200
        except subprocess.CalledProcessError as e:
            print(f"Error pulling from main: {e.output}")
            return jsonify({'success': False, 'error': str(e)}), 500
    
    return jsonify({'success': False}), 400
