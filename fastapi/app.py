from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Hello, Flask API!"})

@app.route('/external-api')
def external_api():
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
