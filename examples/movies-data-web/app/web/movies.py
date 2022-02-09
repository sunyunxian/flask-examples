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
    else:
        flash('Keyword is not validate, please input right keword')
    return render_template('search_result.html', books=data)


@web.get('/book/<mid>/detail')
def movie_detail(mid):
    data = tools.MoviesData(mid).get_data()
    return render_template(
        'book_detail.html', book=data['movies'][0], wishes=[], gifts=[]
    )
