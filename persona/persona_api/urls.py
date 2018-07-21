#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import PeopleList, delete_person

urlpatterns =[
    url(r'^$', PeopleList.as_view(), name='list_people'),
    url(r'^(?P<username>\w+)$', delete_person, name='delete_person'),
]