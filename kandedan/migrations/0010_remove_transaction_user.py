# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kandedan', '0009_auto_20150727_1710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='user',
        ),
    ]
