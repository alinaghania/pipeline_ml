
"""
simple python flask application
""" 

##########################################################################
## Imports
##########################################################################
  
import os
 
from flask import Flask
from flask import request
from flask import render_template
from flask import url_for
from flask.json import jsonify
from flask import request
import logging



##########################################################################
## Application Setup
##########################################################################

app = Flask(__name__)

##########################################################################
## Routes
##########################################################################

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/hello")
def hello():
    """
    Return a hello message
    """
    return jsonify({"hello": "world"})

@app.route("/api/hello/<name>")
def hello_name(name):
    """
    Return a hello message with name
    """
    return jsonify({"hello": name})

@app.route("/api/whoami")
def whoami():
    """
    Return a JSON object with the name, ip, and user agent
    """
    return jsonify(
        name=request.remote_addr,
        ip=request.remote_addr,
        useragent=request.user_agent.string
    )

@app.route("/api/whoami/<name>")
def whoami_name(name):
    """
    Return a JSON object with the name, ip, and user agent
    """
    return jsonify(
        name=name,
        ip=request.remote_addr,
        useragent=request.user_agent.string
    )
@app.route("/testing", methods=['POST'])
def testing():
    pushed_data = request.get_json()  # get the pushed_data from the post request, 
    branch_name = pushed_data.get('ref', '')  # extract the branch name from the pushed data
    if branch_name == 'refs/heads/staging':  # We test on the staging branch 
        os.system('git pull origin staging') # pull the latest changes from the remote repository 
        return jsonify({'success': True}), 200, {'ContentType': 'application/json'}
    
    return jsonify({'success': False}), 400, {'ContentType': 'application/json'} 
    
@app.route("/deployment", methods =['POST'])
def deployment():
    pushed_data = request.get_json()
    branch_name = pushed_data.get('ref','')
    if branch_name == 'refs/heads/main':
        os.system('git pull origin main')
        return jsonify({'success': True}), 200, {'ContentType': 'application/json'}
    
    return jsonify({'success': False}), 400, {'ContentType': 'application/json'}






##########################################################################
## Main
##########################################################################

if __name__ == '__main__':
    app.run()
