# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0007_auto_20160114_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='dateUpdated',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='track',
            name='dateUpdated',
            field=models.DateTimeField(null=True),
        ),
    ]
