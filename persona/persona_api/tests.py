#!/usr/bin/env python
# -*- coding: utf-8 -*-

from persona_api.models import Persona
import pytest
import json


@pytest.mark.django_db
def test_api(client):
    Persona(username='username').save()
    response = client.get('/search/username')
    assert json.loads(response.content)['username'] == 'username'

    response = client.get('/people/')
    assert response.status_code == 200
    assert json.loads(response.content)['results'][0]['username'] == 'username'

    client.delete('/people/username')
    response = client.get('/search/username')
    print(response)
    assert response.status_code == 404