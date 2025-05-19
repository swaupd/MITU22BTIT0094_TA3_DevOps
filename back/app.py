from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
@app.route('/', methods=['POST'])
def login():
    response = request.get_json()
    username = response.get('username')
    password = response.get('password')

    if username == 'admin' and password == 'admin':
        return jsonify("Login successful!"), 200
    else:
        return jsonify("Login Failed"), 401
if __name__ == '__main__':
    app.run(debug=True)
