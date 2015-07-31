# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kandedan', '0003_auto_20150727_1218'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='id',
            new_name='uid',
        ),
    ]
