
from flask import render_template
from . import main
# from ..request import get_news,get_source

@main.route('/')
def source():
    # news_source = get_source()
    title = 'HotTeaNews'
    return render_template('source.html', title = title)