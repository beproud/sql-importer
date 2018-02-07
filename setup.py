#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages

classifiers = [
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Topic :: Software Development',
    'Programming Language :: SQL',
]
keywords = [
    'sql',
]

setup(
    name='sql-importer',
    version='1.0.0',
    description='it enables sql files to be imported as a python module.',
    long_description=open('./README.rst', 'r').read(),
    classifiers=classifiers,
    keywords=', '.join(keywords),
    author='Beproud',
    author_email="righ.m9@gmail.com,crohaco@beproud.jp",
    packages=find_packages(exclude=['tests']),
)
