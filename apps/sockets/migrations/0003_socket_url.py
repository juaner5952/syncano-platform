# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-19 21:29
import jsonfield.fields
from django.db import migrations, models

import apps.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sockets', '0002_socket_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='socket',
            name='install_url',
            field=models.URLField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='socket',
            name='dependencies',
            field=jsonfield.fields.JSONField(blank=True, default=[]),
        ),
        migrations.AlterField(
            model_name='socket',
            name='endpoints',
            field=jsonfield.fields.JSONField(default={}),
        ),
        migrations.AlterField(
            model_name='socketendpoint',
            name='name',
            field=apps.core.fields.LowercaseCharField(max_length=256, unique=True),
        ),
    ]