# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150929_1822'),
    ]

    operations = [
        migrations.CreateModel(
            name='StateCapital',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, blank=True)),
                ('lat', models.FloatField(null=True, blank=True)),
                ('lon', models.FloatField(null=True, blank=True)),
                ('pop', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='state',
            name='capital',
        ),
        migrations.RemoveField(
            model_name='state',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='state',
            name='lon',
        ),
        migrations.RemoveField(
            model_name='state',
            name='pop',
        ),
    ]
