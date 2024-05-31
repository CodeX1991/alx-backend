#!/usr/bin/env python3
"""Get locale from request"""


from flask import Flask, render_template, request, g
from flask_babel import Babel


# Create a flask app
app = Flask(__name__)


class Config:
    """Configuree available language"""
    DEBUG = True
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
app.url_map.strict_slashes = False

babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Determine the best match with our supported lang"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


# Handle an endpoint
@app.route('/')
def index() -> str:
    """Default route"""
    return render_template("3-index.html")


if __name__ == '__main__':
    app.run(debug=True)
