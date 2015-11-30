#!/usr/bin/env python

import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def path(p):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), p)

long_description = ''

try:
    long_description += open(path('README.md')).read()
except IOError:
    pass

version = '0.9'

requirements = [
    'pycurl',
]
tests_requirements = requirements + [
    'nose',
]

setup(name='apiaxle',
      version=version,
      description="Python Client for Apiaxle api",
      long_description=long_description,
      classifiers=[
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Internet :: WWW/HTTP',
          'Topic :: Software Development :: Libraries',
      ],
      keywords='api client apiaxle',
      author='EJ Etherington',
      author_email='eje@vadio.com',
      url='https://github.com/vadio/python-apiaxle',
      license='MIT',
      packages=['apiaxle'],
      install_requires=requirements,
      tests_require=tests_requirements,
      )
