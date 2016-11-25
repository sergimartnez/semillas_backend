# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-12 14:06
from __future__ import unicode_literals

from django.db import migrations, models
import uuid

def gen_uuid(apps, schema_editor):
    MyModel = apps.get_model('services', 'service')
    for row in MyModel.objects.all():
        row.uuid = uuid.uuid4()
        row.save()

class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_service_uuid'),
    ]

    operations = [
        migrations.RunPython(gen_uuid, reverse_code=migrations.RunPython.noop),
    ]
