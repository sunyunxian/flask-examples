from ast import keyword
from flask import jsonify, request
from app.web import web
from app.data import tools


@web.get('/search/')
def search():
    keyword = request.args['keyword']
    data = tools.get_data(keyword)
    return jsonify(data)
