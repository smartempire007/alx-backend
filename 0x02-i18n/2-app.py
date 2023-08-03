#!/usr/bin/env python3
'''Create a get_locale function with the babel.locale selector decorator.
Use request.accept_languages to determine the best match with our
supported languages.'''

from flask import Flask, render_template, request
from flask_babel import Babel, gettext


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
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Returns the selected locale based on the request.

    Returns:
        str: The selected locale.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Renders the index template.

    Returns:
        str: The rendered HTML content.
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
