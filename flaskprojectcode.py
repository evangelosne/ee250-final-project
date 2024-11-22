from flask import Flask, jsonify, request
from FinalProject import trending_channels

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Sifa and Evangelos' EE250 Project!"

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(trending_channels)

@app.route('/notes', methods=['POST'])
def submit_note():
    submitted_data = request.json
    return jsonify({"received": submitted_data, "message": "Data received successfully!"})


if __name__ == '__main__':
    app.run(debug=True)

