# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_statecapital_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statecapital',
            name='state',
        ),
        migrations.AddField(
            model_name='statecapital',
            name='state',
            field=models.ManyToManyField(to='main.State'),
        ),
    ]
