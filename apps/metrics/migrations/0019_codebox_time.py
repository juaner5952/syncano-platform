# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-18 13:42
from django.db import migrations, models
from django.utils import timezone


class Migration(migrations.Migration):

    dependencies = [
        ('metrics', '0018_cleanup_nulls'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dayaggregate',
            name='source',
            field=models.CharField(choices=[('api', 'api call'), ('cbx', 'script execution time')], max_length=3),
        ),
        migrations.AlterField(
            model_name='houraggregate',
            name='source',
            field=models.CharField(choices=[('api', 'api call'), ('cbx', 'script execution time')], max_length=3),
        ),
        migrations.AlterField(
            model_name='minuteaggregate',
            name='source',
            field=models.CharField(choices=[('api', 'api call'), ('cbx', 'script execution time')], max_length=3),
        ),
        migrations.RunSQL(
            """
            UPDATE metrics_minuteaggregate SET value = value * 12 WHERE timestamp >= '{start}' AND source='cbx';
            UPDATE metrics_houraggregate SET value = value * 12 WHERE timestamp >= '{start}' AND source='cbx';
            UPDATE metrics_dayaggregate SET value = value * 12 WHERE timestamp >= '{start}' AND source='cbx';
            """.format(start=timezone.now().replace(day=1).date())
        ),
    ]
