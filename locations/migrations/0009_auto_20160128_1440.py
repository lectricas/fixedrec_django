# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0008_auto_20160128_0049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='point',
            name='dateUpdated',
        ),
        migrations.AlterField(
            model_name='track',
            name='owner',
            field=models.TextField(null=True),
        ),
    ]
