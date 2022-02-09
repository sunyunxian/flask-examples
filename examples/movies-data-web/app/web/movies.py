from flask import jsonify, request, render_template, flash
from app.web import web
from app.data import tools
from app.forms.movies import SearchForm


@web.get('/book/search')
def search():
    data = {}
    form = SearchForm(request.args)
    if form.validate():
        keyword = form.keyword.data
        data = tools.MoviesData(keyword).get_data()
        print(data)
    else:
        flash('Keyword is not validate, please input right keword')
    return render_template('search_result.html', books=data)


@web.get('/book/<id>/detail')
def movie_detail(id):
    pass
