#!/usr/bin/env python3
"""A simple Flask app that demonstrates internationalization and localization
features using Flask-Babel.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config(object):
    """Configuration class for the Flask app.

    Attributes:
        LANGUAGES (list): List of supported languages.
        BABEL_DEFAULT_LOCALE (str): Default locale for the app.
        BABEL_DEFAULT_TIMEZONE (str): Default timezone for the app.
    """

    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """Get the user dictionary based on the login ID provided in the
    request args.

    Returns:
        dict or None: User dictionary or None if the ID cannot be found.
    """
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request():
    """Callback function executed before each request.

    It sets the `g.user` object to the user dictionary
    retrieved using `get_user()`.
    """
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale():
    """Determine the locale for the current request.

    It first checks if the locale is specified in the request args. If not,
    it falls back to the best match locale from the accept
    languages of the request.

    Returns:
        str: The selected locale.
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Render the index template.

    Returns:
        str: Rendered HTML template.
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
