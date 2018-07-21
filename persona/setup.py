#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='persona API',
    version='0.0.1',
    description='This a tech challenge for CACI',
    url='https://github.com/Quan-Yuan/persona-api',
    author='quan.yuan',
    author_email='quan.yuan@outlook.com',
    packages=find_packages(include=['persona', 'persona.*']),
    install_requires=[
        'Django',  # TODO: pin the version
        'djangorestframework',
        'django-rest-swagger',
        'Markdown',
        'psycopg2',
    ]
)