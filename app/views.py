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

    # Getting business sources
    business_sources = get_sources('business')

    return render_template('index.html', title = title, business = business_sources)