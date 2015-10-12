# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20150930_2118'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name_plural': 'cities'},
        ),
        migrations.AlterField(
            model_name='city',
            name='lat',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='lon',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
