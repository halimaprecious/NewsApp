
from flask import render_template
from . import main
from ..request import get_source,get_news

@main.route('/')
def source():
    news_source = get_source()
    title = 'QuickUpdates'
    return render_template('source.html', title = title,sources = news_source)

@main.route('/articles')
def articles():
    news = get_news()
    title = 'HotTeaNews'

    return render_template('news.html',articles = news ,title = title)