# app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/data')
def data():
    return "Hello from Python!"

if __name__ == "__main__":
    app.run(debug=True)
