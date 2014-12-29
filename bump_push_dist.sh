#!/bin/bash
versioner +revision
git push
python setup.py sdist upload

