VERSION = '0.1'

from flask import render_template
from gibe2.environment import app, assets, pages
from gibe2.util import datedposts

app.template_filter('datedposts')(datedposts)

site_context = dict(
    assets=assets,
)
@app.context_processor
def context():
    return dict(site=site_context)

@app.route('/')
def index():
    articles = [p for p in pages if 'published' in p.meta]
    # Show the 10 most recent articles, most recent first.
    articles.sort(reverse=True, key=lambda p: p.meta['published'])
    return render_template('index.html', pages=articles)

@app.route('/<path:path>.html')
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)

__all__ = []
