from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/hello/', methods=['GET'])
def welcome():
    return "Hello World!"



if __name__ == '__main__':
    app.run(debug=False)
