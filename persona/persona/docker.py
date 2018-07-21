#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
For docker
"""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'people',
        'USER': "docker",
        "PASSWORD": "mysecretpassword",
        "HOST": "database",
        "PORT": "5432"
    }
}