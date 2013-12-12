import argparse
from os import getcwd
from os.path import join
import sys


from gibe2 import assets, site_context
from gibe2.environment import app, freezer

class Config(object):
    def __init__(self, **kw):
        for k, v in kw.items():
            setattr(self, k, v)

    def register_asset(self, *args, **kw):
        print args, kw
        assets.register(*args, **kw)

    def context_update(self, *args, **kw):
        for d in args:
            site_context.update(d)
        site_context.update(kw)

def appconfig(args):
    webroot = join(args.startcwd, args.webroot)
    config = Config(
        FLATPAGES_ROOT = join(
            webroot,
            'posts/'
        ),
        FLATPAGES_EXTENSION = '.md',
        FREEZER_DESTINATION = join(
            webroot,
            "build"
        ),
    )

    app.config.from_object(config)
    app.static_folder = join(webroot, "static")
    app.template_folder = join(webroot, "templates")

    configfile = join(webroot, "config.py")
    execfile(configfile, dict(config=config))

def freeze():
    freezer.freeze()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("webroot", help="Where posts are found")
    parser.add_argument("--freeze", action="store_true", help="Freeze to an export directory")
    args = parser.parse_args()
    args.startcwd = getcwd()

    appconfig(args)
    if args.freeze:
        sys.exit(freeze())
    app.run(host="0.0.0.0", debug=True)

if __name__ == "__main__":
    main()
