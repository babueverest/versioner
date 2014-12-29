#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "versioner",
    version = "0.0.1",
    author = "José Tomás Tocino",
    author_email = "josetomas.tocino@gmail.com",
    description = ("A very basic command-line tool and library to keep "
        "track of the version of your project."),
    license = "GPLv2",
    keywords = "version versioning tool revision mayor minor",
    url = "http://packages.python.org/an_example_pypi_project",
    packages=['versioner', 'tests'],
    scripts = ['versioner/versioner.py'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ],
    entry_points = {
        'console_scripts': [
            'versioner = versioner:main'
        ]
    }
)