# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20150930_1720'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statecapital',
            name='state',
        ),
        migrations.AddField(
            model_name='statecapital',
            name='state',
            field=models.OneToOneField(null=True, blank=True, to='main.State'),
        ),
    ]
