VERSION = '0.1'

from gibe2.environment import app, assets
from gibe2.util import datedposts

app.template_filter('datedposts')(datedposts)

site_context = dict(
    assets=assets,
)

@app.context_processor
def context():
    return dict(site=site_context)

__all__ = []
