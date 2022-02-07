from flask import jsonify
from app.api.v2 import v2_bp


@v2_bp.get('/')
def index():
    return jsonify({'home': "v2"})
