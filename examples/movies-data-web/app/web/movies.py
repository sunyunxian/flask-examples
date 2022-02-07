from flask import jsonify, request
from app.web import web
from app.data import tools
from app.forms.movies import SearchForm


@web.get('/search/')
def search():

    form = SearchForm(request.args)
    if form.validate():
        keyword = form.keyword.data
        print('Validate right')
        data = tools.get_data(keyword)
        return jsonify(data)
    else:
        print('Validate wrong')
        return jsonify({'msg': 'Validate wrong'})
