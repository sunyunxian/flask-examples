from flask import Flask, jsonify

app = Flask('__name__')


@app.get('/')
def index():
    data = {'home': 'index'}
    return jsonify(data)
