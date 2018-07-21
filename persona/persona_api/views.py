#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .models import Persona
from .serializers import PersonaSerializer


class PeopleList(ListAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer


@api_view(['GET'])
def search_person(request, username):
    """
    search person according to username, return the detail if the people is in databse otherwise 404
    """
    if request.method == 'GET':
        try:
            person = Persona.objects.get(username=username)
        except Persona.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PersonaSerializer(person)
        return Response(serializer.data)


@api_view(['DELETE'])
def delete_person(request, username):
    """
    delete person with given username, 404 if person does not exist.
    """
    if request.method == 'DELETE':
        try:
            person = Persona.objects.get(username=username)
        except Persona.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
