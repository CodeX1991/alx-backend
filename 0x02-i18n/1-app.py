#!/usr/bin/env python3
"""A basic Babel setup"""


from flask import Flask, render_template
from flask_babel import Babel


# Create a flask app
app = Flask(__name__)


class Config:
    """Configuree available language"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)

# Handle an endpoint
@app.route('/')
def index():
    """Default route"""
    return render_template("1-index.html")


if __name__ == '__main__':
    app.run(debug=True)
