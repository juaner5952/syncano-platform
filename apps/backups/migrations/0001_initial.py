# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-26 10:29
import django.db.models.deletion
import jsonfield.fields
from django.conf import settings
from django.db import migrations, models

import apps.backups.models
import apps.core.fields
from apps.core.backends.storage import default_storage


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instances', '0010_remove_instance_old_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Backup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metadata', jsonfield.fields.JSONField(blank=True, default={})),
                ('description', models.TextField(blank=True, max_length=256)),
                ('label', models.CharField(blank=True, max_length=64)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.SmallIntegerField(choices=[(-2, 'aborted'), (-1, 'error'), (0, 'scheduled'), (1, 'running'), (2, 'uploading'), (3, 'success')], default=0)),
                ('archive', models.FileField(upload_to=apps.backups.models.backup_filename, storage=default_storage)),
                ('size', models.IntegerField(null=True)),
                ('_is_live', apps.core.fields.LiveField(db_index=True, default=True)),
                ('instance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='backups', to='instances.Instance')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='backups', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Restore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=256)),
                ('label', models.CharField(blank=True, max_length=64)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.SmallIntegerField(choices=[(-2, 'aborted'), (-1, 'error'), (0, 'scheduled'), (1, 'running'), (3, 'success')], default=0)),
                ('backup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backups.Backup')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('target_instance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instances.Instance')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]
