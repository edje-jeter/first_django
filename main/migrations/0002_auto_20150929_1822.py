# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='abbrev',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='capital',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='lat',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='lon',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='name',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='pop',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
