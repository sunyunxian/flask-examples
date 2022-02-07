from flask import Blueprint

v2_bp = Blueprint('v2', __name__)

from app.api.v2 import user
