#!/bin/sh
# build.sh [SETUPTOOLS_ARGS]: clean old stuff and build a wheel

set -eux
pwd
ls
rm -rf build dist *.egg-info
python -c 'import sys; assert sys.version_info > (3,), sys.version'
python setup.py bdist_wheel "$@"
