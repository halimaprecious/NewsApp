import urllib.request,json
from .models import Source,Article

api_key = None
base_url = None

def configure_request(app):
    global api_key, base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']

def get_source():
    source_base_url = 'https://newsapi.org/v2/top-headlines/sources?apiKey=0cff81b85884415aa6f77fb081c448f8'.format(api_key)

    with urllib.request.urlopen(source_base_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None

        if get_source_response['sources']:
            source_results_list = get_source_response['sources']
            source_results = produce_results(source_results_list)

            return source_results

def produce_results(source_list):
    source_results =[]
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        language = source_item.get('language')
        country = source_item.get('country')
        url = source_item.get('url')

        source_object = Source(id, name, description, language, country, url,)
        source_results.append(source_object)
        
    return source_results

# Articles request
def get_news():
    get_news_url = base_url.format(api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)

            return news_results

def process_results(news_list):
    news_results = []

    for news_item in news_list:
        title = news_item.get('title')
        description = news_item.get('description')
        url = news_item.get('url')
        urlToImage = news_item.get('urlToImage')
        content = news_item.get('content')
        publishedAt= news_item.get('publishedAt')

        news_object = Article(title, description,url, urlToImage, content, publishedAt)
        news_results.append(news_object)

    return news_results