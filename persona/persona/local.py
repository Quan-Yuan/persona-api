#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
DATABASE setttings for running in local, it require data base people created,  postgres installed
"""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'people',
    }
}