from sys import prefix
from flask import Blueprint
from app.api.v1 import v1_bp
from app.api.v2 import v2_bp

api_bp = Blueprint('api', __name__)

api_bp.register_blueprint(v1_bp, url_prefix='/v1')
api_bp.register_blueprint(v2_bp, url_prefix='/v2')
