#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This script will ingest data from a json file
"""
import json
from fileinput import hook_compressed

from django.core.management.base import BaseCommand
from django.db.transaction import atomic
from persona_api.models import Persona


class PeopleFromJson(BaseCommand):
    help = "Ingest data to people database by using json"

    def add_arguments(self, parser):
        parser.add_argument('filename')

    def handle(self, *args, **options):
        with hook_compressed(options['filename']) as fp:
            all_data = json.load(fp)
        with atomic():
            for info in all_data:
                person = Persona(**info)
                person.save()
