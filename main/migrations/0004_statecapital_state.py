# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20150930_1624'),
    ]

    operations = [
        migrations.AddField(
            model_name='statecapital',
            name='state',
            field=models.ForeignKey(blank=True, to='main.State', null=True),
        ),
    ]
