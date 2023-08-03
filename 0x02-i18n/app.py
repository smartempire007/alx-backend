#!/usr/bin/env python3
"""A simple Flask app that demonstrates internationalization and localization
features using Flask-Babel.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
from pytz import timezone
import pytz.exceptions
from datetime import datetime
import locale


class Config(object):
    """Configuration class for the Flask app.

    Attributes:
        LANGUAGES (list): A list of supported languages.
        BABEL_DEFAULT_LOCALE (str): The default locale to use.
        BABEL_DEFAULT_TIMEZONE (str): The default timezone to use.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Configure the Flask app
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
    """Returns the user dictionary based on the provided login ID.
    Returns:
        dict or None: The user dictionary if found, None otherwise.
    """
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id), None)
    return None


@app.before_request
def before_request() -> None:
    """Performs actions before each request is processed.
    """
    user = get_user()
    g.user = user

    time_now = pytz.utc.localize(datetime.utcnow())
    time = time_now.astimezone(timezone(get_timezone()))
    locale.setlocale(locale.LC_TIME, (get_locale(), 'UTF-8'))
    time_format = "%b %d, %Y %I:%M:%S %p"
    g.time = time.strftime(time_format)


@babel.localeselector
def get_locale():
    """Returns the selected locale based on the request.

    Returns:
        str: The selected locale.
    """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    if g.user:
        locale = g.user.get('locale')
        if locale and locale in app.config['LANGUAGES']:
            return locale

    locale = request.headers.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """Returns the selected timezone based on the request.

    Returns:
        str: The selected timezone.
    """
    tzone = request.args.get('timezone', None)
    if tzone:
        try:
            return timezone(tzone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    if g.user:
        try:
            tzone = g.user.get('timezone')
            return timezone(tzone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    default_tz = app.config['BABEL_DEFAULT_TIMEZONE']
    return default_tz


@app.route('/')
def index():
    """Renders the index template.

    Returns:
        str: The rendered HTML content.
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
