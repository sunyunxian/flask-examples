from flask import Blueprint

web = Blueprint(name='web', import_name=__name__)

from app.web import movies
