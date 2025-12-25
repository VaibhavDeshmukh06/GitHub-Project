from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = os.path.join(os.path.dirname(__file__), 'data.json')

@app.route('/')
def home():
    return "welcome to the page"

@app.route('/api')
def get_data():
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)      
    return jsonify(data)         

if __name__ == '__main__':
    app.run(debug=True)
