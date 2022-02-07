from flask import jsonify
from app.api.v1 import v1_bp


@v1_bp.get('/')
def index():
    return jsonify({'home': "v1"})
