#!/usr/bin/env python3
"""Force locale with URL parameter"""


from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Optional


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


@babel.localeselector
def get_locale() -> Optional[str]:
    """Determine the best match with our supported lang"""
    locale: Optional[str] = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.before_request
def before_request() -> None:
    """Set the local for the current request in the global object"""
    g.locale = get_locale()


# Handle an endpoint
@app.route('/')
def index() -> str:
    """Default route"""
    return render_template("4-index.html")


if __name__ == '__main__':
    app.run(debug=True)
