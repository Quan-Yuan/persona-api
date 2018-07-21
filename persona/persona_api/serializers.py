#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Persona


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'
