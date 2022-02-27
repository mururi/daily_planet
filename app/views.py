from flask import render_template
from app import app
from .request import get_sources

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


    return render_template('index.html', title = title, business = business_sources, entertainment = entertainment_sources, general = general_sources, health = health_sources)