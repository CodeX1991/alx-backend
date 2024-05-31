#!/usr/bin/env python3
"""A basic FlaskApp"""


from flask import Flask, render_template


# Create a flask app
app = Flask(__name__)

# Handle an endpoint
@app.route('/')
def index():
    """Default route"""
    return render_template("0-index.html")


if __name__ == '__main__':
    app.run(debug=True)
