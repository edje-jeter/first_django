# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('abbrev', models.CharField(max_length=255)),
                ('capital', models.CharField(max_length=255)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('pop', models.IntegerField()),
            ],
        ),
    ]
