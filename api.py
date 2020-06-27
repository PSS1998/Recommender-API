import flask
from flask import request, jsonify, render_template 
import subprocess
import json
import ast

app = flask.Flask(__name__)


@app.route('/api', methods=['GET'])
def api():
	if 'type' in request.args:
		typeM = str(request.args['type'])
	if 'name' in request.args:
		name = str(request.args['name'])
		name.replace("+", " ")
	process = subprocess.run(["/home/ubuntu/w/recommender/getRecommendation.py", name, typeM], universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	output = process.stdout
	json_output = ast.literal_eval(output)
	return jsonify(output)

@app.route('/result', methods=['GET'])
def api():
	if 'type' in request.args:
		typeM = str(request.args['type'])
	if 'name' in request.args:
		name = str(request.args['name'])
		name.replace("+", " ")
	process = subprocess.run(["/home/ubuntu/w/recommender/getRecommendation.py", name, typeM], universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	output = process.stdout
	json_output = ast.literal_eval(output)
	return render_template('results.html', data = json_output)

@app.route('/', methods=['GET'])
def home():
	return render_template("home.html")


app.run(host="0.0.0.0")
