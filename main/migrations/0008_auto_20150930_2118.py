# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='zipc',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
