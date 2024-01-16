from flask import Blueprint, jsonify, request
import subprocess

deployment_blueprint = Blueprint('deployment', __name__)
testing_blueprint = Blueprint('testing', __name__)

# Paths to your scripts
PATH_TO_TEST_SCRIPT = '/Users/alina/vs-project/project/pipeline_ml/script_run_test.sh'
PATH_TO_LAUNCH_SCRIPT = '/Users/alina/vs-project/project/pipeline_ml/script_launch_app.sh'

@deployment_blueprint.route("/", methods=['POST'])
def deployment():
    try:
        # Extract the branch name from the payload
        data = request.json
        branch_name = data['ref'].split('/')[-1]

        # Check if the push was to the main branch
        if branch_name == "main":
            # Run the deployment script
            subprocess.run([PATH_TO_LAUNCH_SCRIPT,branch_name], check=True)
            return jsonify({'success': True, 'message': 'Deployment started.'}), 200
        else:
            return jsonify({'success': False, 'message': 'Deployment skipped for non-main branch.'}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@testing_blueprint.route("/", methods=['POST'])
def testing():
    try:
        # Extract the branch name from the payload
        data = request.json
        branch_name = data['ref'].split('/')[-1]

        # Check if the push was to the staging branch
        if branch_name == "staging":
            # Run the testing script
            subprocess.run([PATH_TO_TEST_SCRIPT,branch_name], check=True)
            return jsonify({'success': True, 'message': 'Testing started.'}), 200
        else:
            return jsonify({'success': False, 'message': 'Testing skipped for non-staging branch.'}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({'success': False, 'message': str(e)}), 500
