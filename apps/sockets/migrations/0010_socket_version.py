# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-12-27 16:41
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sockets', '0009_remove_obsolete_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='socket',
            name='version',
            field=models.CharField(default='0.1', max_length=32),
        ),
    ]
