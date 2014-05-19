# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
Flask-Via
---------

Flask-Via is a url routing register designed for larger Flask applications
allowing developers to much more cleanly manage routes across your
application.
"""

# Temporary patch for issue reported here:
# https://groups.google.com/forum/#!topic/nose-users/fnJ-kAUbYHQ
import multiprocessing  # noqa
import os
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


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
    with open(filename) as f:
        for line in f.readlines():
            if not line or line.startswith('#'):
                continue
            requirements.append(line.strip())
    return requirements

# Get current working directory

try:
    SETUP_DIRNAME = os.path.dirname(__file__)
except NameError:
    SETUP_DIRNAME = os.path.dirname(sys.argv[0])

# Change to current working directory

if SETUP_DIRNAME != '':
    os.chdir(SETUP_DIRNAME)

# Requirements

INSTALL_REQUIREMENTS = read_requirements('REQS.txt')
TESTING_REQUIREMENTS = read_requirements('REQS.TESTING.txt')
DEVELOP_REQUIREMENTS = read_requirements('REQS.DEVELOP.txt') \
    + TESTING_REQUIREMENTS

# Include the Change Log on PyPi

long_description = open('README.rst').read() + '\n\r.. include:: CHANGELOG.rst'

# Setup

setup(
    name='Flask-Via',
    version=open('VERSION').read().strip(),
    author='SOON_',
    author_email='dorks@thisissoon.com',
    url='http://flask-via.thisissoon.com',
    description='Flask-Via adds a cleaner method for defining routes '
                'to your Flask views, inspired by Django urls.',
    long_description=long_description,
    packages=find_packages(
        exclude=[
            'tests'
        ]),
    include_package_data=True,
    zip_safe=False,
    # Dependencies
    install_requires=INSTALL_REQUIREMENTS,
    extras_require={
        'develop': DEVELOP_REQUIREMENTS
    },
    # Testing
    tests_require=TESTING_REQUIREMENTS,
    cmdclass={
        'test': PyTest
    },
    # Dependencies not hosted on PyPi
    dependency_links=[],
    # Classifiers for Package Indexing
    # Entry points, for example Flask-Script
    entry_points={},
    classifiers=[
        'Framework :: Flask',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 5 - Production/Stable',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content'])
