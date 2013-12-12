#!/bin/bash

set -e
set -u

cd `dirname $0`
if [ ! -d .env ]; then
    python scripts/virtualenv.py --no-site-packages --distribute .env
fi
if [ ! -e activate ]; then
    ln -s .env/bin/activate activate
fi

# activate plays fast and loose with variables
set +u
source activate
set -u

python setup.py develop
