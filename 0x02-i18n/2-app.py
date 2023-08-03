#!/usr/bin/env python3
'''Create a get_locale function with the babel.localeselector decorator.
Use request.accept_languages to determine the best match with our
supported languages.'''

from flask import Flask, render_template, request
from flask_babel import Babel, gettext


class Config(object):
    '''Config class'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    '''get_locale method'''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
