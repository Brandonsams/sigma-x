import json
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	return jsonify({'name': 'alice',
					'email': 'alice@outlook.com'})

app.run()