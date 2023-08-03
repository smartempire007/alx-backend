#!/usr/bin/env python3
'''Use the _ or gettext function to parametrize your templates.
Use the message IDs home_title and home_header.'''

from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """Configuration class for the Flask app.
    Attributes:
        LANGUAGES (list): A list of supported languages.
        BABEL_DEFAULT_LOCALE (str): The default locale to use.
        BABEL_DEFAULT_TIMEZONE (str): The default timezone to use.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale():
    '''get_locale method'''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    '''index method'''
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
