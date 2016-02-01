# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0006_track_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='track',
            options={'ordering': ('dateCreated', 'owner')},
        ),
    ]
