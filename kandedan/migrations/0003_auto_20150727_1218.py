# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kandedan', '0002_auto_20150726_2329'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='type',
            new_name='trans_type',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='type',
            new_name='user_type',
        ),
    ]
