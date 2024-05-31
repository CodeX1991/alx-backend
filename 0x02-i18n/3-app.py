#!/usr/bin/env python3
"""Get locale from request"""


from flask import Flask, render_template, request, g
from flask_babel import Babel, _


# Create a flask app
app = Flask(__name__)


class Config:
    """Configuree available language"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """Determine the best match with our supported lang"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.before_request
def before_request():
    """Make get_locale global"""
    g.locale = get_locale()


# Handle an endpoint
@app.route('/')
def index():
    """Default route"""
    return render_template("3-index.html")


if __name__ == '__main__':
    app.run(debug=True)
