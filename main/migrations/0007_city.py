# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20150930_1747'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zipc', models.FloatField(null=True, blank=True)),
                ('lat', models.FloatField(null=True, blank=True)),
                ('lon', models.FloatField(null=True, blank=True)),
                ('name', models.CharField(max_length=255, null=True, blank=True)),
                ('abbrev', models.CharField(max_length=255, null=True, blank=True)),
                ('county', models.CharField(max_length=255, null=True, blank=True)),
                ('state', models.ForeignKey(blank=True, to='main.State', null=True)),
            ],
        ),
    ]
