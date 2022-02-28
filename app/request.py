from app import app
import urllib.request, json
from .models import source, article
from datetime import datetime

Source = source.Source
Article = article.Article

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the Sources base url
sources_base_url = app.config['NEWS_SOURCES_BASE_URL']

# Getting the Articles base url
articles_base_url = app.config['NEWS_ARTICLES_BASE_URL']

def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''

    get_sources_url = sources_base_url.format(category, api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources_results(sources_results_list)

    return sources_results

def process_sources_results(sources_list):
    '''
    Function that processes the sources result list and transform them into a list of Objects with the elements/properties we need

    Args:
        sources_list: A list of dictionaries that contain source details
    Returns:
        sources_results: A list of source objects
    '''

    sources_results = []

    for source_item in sources_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')

        source_object = Source(id, name, description, url, category, language, country)
        sources_results.append(source_object)

    return sources_results

def get_articles(id):
    '''
    Function that gets the json response to our url request
    '''

    get_articles_url = articles_base_url.format(id, api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_result_list = get_articles_response['articles']
            articles_results = process_articles_results(articles_result_list)

    return articles_results

def process_articles_results(articles_list):
    '''
    Function that processes the articles result list and transform them into a list of Objects with the elements/properties we need

    Args:
        articles_list: A list of dictionaries that contain article details
    Returns:
        articles_results: A list of article objects
    '''

    articles_results = []

    for article_item in articles_list:
        id = article_item.get('id')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        rawDate = article_item.get('publishedAt')

        date_object = datetime.strptime(rawDate, '%Y-%m-%dT%H:%M:%SZ')
        publishedAt = date_object.strftime('%d.%m.%Y')
        print(publishedAt)

        if urlToImage and description:
            article_object = Article(id, author, title, description, url, urlToImage, publishedAt)
            articles_results.append(article_object)

    return articles_results