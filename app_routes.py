from flask import Blueprint, jsonify, request
import subprocess

deployment_blueprint = Blueprint('deployment', __name__)
testing_blueprint = Blueprint('testing', __name__)

# Path to your scripts
PATH_TO_TEST_SCRIPT = '/Users/alina/vs-project/project/pipeline_ml/script_run_test.sh'
PATH_TO_LAUNCH_SCRIPT = '/Users/alina/vs-project/project/pipeline_ml/script_launch_app.sh'


@testing_blueprint.route("", methods=['POST'])
def testing():
    try:
        # Extraire le nom de la branche à partir des données de la requête
        data = request.json
        branch_name = data['ref'].split('/')[-1]  # 'ref' est généralement sous la forme 'refs/heads/nom_de_la_branche'

        # Exécuter le script avec le nom de la branche
        subprocess.run([PATH_TO_TEST_SCRIPT, branch_name], check=True)
        return jsonify({'success': True, 'message': 'Tests started.'}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({'success': False, 'message': str(e)}), 500


@deployment_blueprint.route("", methods=['POST'])
def deployment():
    try:
        # Extraire le nom de la branche à partir des données de la requête
        data = request.json
        branch_name = data['ref'].split('/')[-1]

        # Exécuter le script avec le nom de la branche
        subprocess.run([PATH_TO_LAUNCH_SCRIPT, branch_name], check=True)
        return jsonify({'success': True, 'message': 'Deployment started.'}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({'success': False, 'message': str(e)}), 500

