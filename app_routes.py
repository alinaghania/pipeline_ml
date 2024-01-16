from flask import Blueprint, jsonify, request
import subprocess

deployment_blueprint = Blueprint('deployment', __name__)
testing_blueprint = Blueprint('testing', __name__)

# Path to your scripts
PATH_TO_TEST_SCRIPT = '/Users/alina/vs-project/project/pipeline_ml/script_launch_app.sh'
PATH_TO_LAUNCH_SCRIPT = '/Users/alina/vs-project/project/pipeline_ml/script_run_test.sh'

@testing_blueprint.route("/", methods=['POST'])
def testing():
    try:
        # Run the test script
        subprocess.run([PATH_TO_TEST_SCRIPT], check=True)
        return jsonify({'success': True, 'message': 'Tests started.'}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@deployment_blueprint.route("/", methods=['POST'])
def deployment():
    try:
        # Run the deployment script
        subprocess.run([PATH_TO_LAUNCH_SCRIPT], check=True)
        return jsonify({'success': True, 'message': 'Deployment started.'}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({'success': False, 'message': str(e)}), 500
