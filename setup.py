"""
gibe2
"""

from __future__ import with_statement
import re
import os.path
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__),
                       'gibe2', '__init__.py')) as init_py:
    VERSION = re.search("VERSION = '([^']+)'", init_py.read()).group(1)


setup(
    name='gibe2',
    version=VERSION,
    #url='',
    license='BSD',
    author='Neil Blakey-Milner',
    author_email='nbm@nxsy.org',
    description='A static-site generator for a web site.',
    long_description=__doc__,
    packages=find_packages(),
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask == 0.9',
        'Frozen-Flask == 0.9',
        'Flask-Assets==0.8',
        'Flask-FlatPages==0.3',
        'Pygments==1.5',
    ],
    entry_points={
        'console_scripts': ['gibe2 = gibe2.__main__:main'],
    },
)
