
from flask import render_template
from . import main
from ..request import get_source

@main.route('/')
def source():
    news_source = get_source()
    title = 'QuickUpdates'
    return render_template('source.html', title = title,sources = news_source)