#!/usr/bin/env python3
"""Mock logging in"""


from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Optional, Dict, Union


class Config:
    """Configuree available language"""
    DEBUG = True
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


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


def get_user() -> Union[Dict, None]:
    """Retrieves a user based on a user id"""
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request() -> None:
    """Set the local for the current request in the global object"""
    g.user = get_user()
    g.locale = get_locale()


@babel.localeselector
def get_locale() -> Optional[str]:
    """Determine the best match with our supported lang"""
    locale: Optional[str] = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']

    header_locale: Optional[str] = request.headers.get('locale', '')
    if header_locale in app.config['LANGUAGES']:
        return header_locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


# Handle an endpoint
@app.route('/')
def index() -> str:
    """Default route"""
    return render_template("6-index.html")


if __name__ == '__main__':
    app.run(debug=True)
