from flask import Flask, render_template
from app_routes import deployment_blueprint, testing_blueprint
from flask import request
from flask.json import jsonify


app = Flask(__name__)

# Register blueprints with prefixes to avoid route conflicts
app.register_blueprint(deployment_blueprint, url_prefix='/deployment')
app.register_blueprint(testing_blueprint, url_prefix='/testing')

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
