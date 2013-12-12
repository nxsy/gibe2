from flask import Flask
from flask.ext.assets import Environment
from flask.ext.flatpages import FlatPages

from flask_frozen import Freezer

app = Flask(__name__)
pages = FlatPages(app)
freezer = Freezer(app, with_static_files=False)

assets = Environment(app)
assets.versions = 'hash'

__ALL__ = (
    'app',
    'assets',
    'freezer',
    'pages',
)
