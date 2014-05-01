# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
Flask-Via
---------

Flask-Via is a url routing register designed for larger Flask applications
allowing developers to much more cleanly manage routes across your
application.
"""

import os
import sys

from setuptools import setup, find_packages

root = os.path.abspath(os.path.join(os.path.dirname(__file__)))
sys.path.append(os.path.join(root, 'flask_via'))
extras_require = {}

import flask_via


def read_requirements(filename):
    """ Read requirements file and process them into a list
    for usage in the setup function.

    Arguments
    ---------
    filename : str
        Path to the file to read line by line

    Returns
    --------
    list
        list of requirements::

            ['package==1.0', 'thing>=9.0']
    """

    requirements = []
    try:
        with open(filename) as f:
            for line in f.readlines():
                line = line.strip()
                if not line or line.startswith('#') or line == '':
                    continue
                requirements.append(line)
    except IOError:
        pass
    return requirements

# Get current directory where setup is running
try:
    SETUP_DIRNAME = os.path.dirname(__file__)
except NameError:
    SETUP_DIRNAME = os.path.dirname(sys.argv[0])

# Change directory
if SETUP_DIRNAME != '':
    os.chdir(SETUP_DIRNAME)

# Paths to requirement files
REQUIREMENTS_FILE = os.path.join('REQS.txt')
TEST_REQUIREMENTS_FILE = os.path.join('REQS_TEST.txt')
DEV_REQUIREMENTS_FILE = os.path.join('REQS_DEV.txt')

# Development requirements
extras_require['develop'] = read_requirements(DEV_REQUIREMENTS_FILE) + \
    read_requirements(TEST_REQUIREMENTS_FILE)

# Setup function
setup(
    name='Flask-Via',
    version=flask_via.__version__,
    author=flask_via.__author__,
    author_email=flask_via.__author_email__,
    url='https://github.com/thisissoon/Flask-Via',
    description='Flask-Via adds Django style url routing configuration.',
    long_description=open('README.rst').read(),
    packages=find_packages(
        exclude=[
            'tests'
        ]),
    include_package_data=True,
    zip_safe=False,
    # Dependencies
    setup_requires=read_requirements(TEST_REQUIREMENTS_FILE),
    install_requires=read_requirements(REQUIREMENTS_FILE),
    extras_require=extras_require,
    # Tests
    tests_require=read_requirements(TEST_REQUIREMENTS_FILE),
    test_suite='nose.collector',
    # Dependencies not hosted on PyPi
    dependency_links=[],
    # Entry point functions
    entry_points={},
    # Classifiers for Package Indexing
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content'])
