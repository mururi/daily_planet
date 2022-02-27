from flask import render_template
from app import app
from .request import get_articles, get_sources

# Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    title = 'Daily Planet'

    # Getting business news sources
    business_sources = get_sources('business')

    # Getting entertainment news sources
    entertainment_sources = get_sources('entertainment')

    # Getting general news sources
    general_sources = get_sources('general')

    # Getting health news sources
    health_sources = get_sources('health')

    # Getting science news sources
    science_sources = get_sources('science')

    # Getting sports news sources
    sports_sources = get_sources('sports')

    # Getting technology news sources
    technology_sources = get_sources('technology')


    return render_template('index.html', title = title, business = business_sources, entertainment = entertainment_sources, general = general_sources, health = health_sources, science = science_sources, sports = sports_sources, technology = technology_sources)


@app.route('/source/<id>')
def articles(id):
    '''
    View articles page function that returns the articles page that displays articles from a given source
    '''

    articles = get_articles(id)
    title = f'Daily Planet | {id}'

    return render_template('articles.html', articles = articles, title = title)