from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

#from FinalProject import trending_channels


@app.route('/')
def home():
    with open('home.html', 'r') as html_file:  # Ensure home.html is in the same folder as this script
        content = html_file.read()
    return content
   # return "Welcome to Sifa and Evangelos' EE250 Project!"

@app.route('/youtuberData', methods=['GET'])
def get_data():
    trending_channels = ["hello", "bye", "random", "items"]
    return jsonify(trending_channels)
        

@app.route('/notes', methods=['POST'])
def submit_note():
    submitted_data = request.json
    return jsonify({"received": submitted_data, "message": "Data received successfully!"})


if __name__ == '__main__':
    app.run(debug=True)

