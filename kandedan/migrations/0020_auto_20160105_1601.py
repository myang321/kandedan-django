# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kandedan', '0019_transaction_group_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='group_id',
            new_name='group',
        ),
    ]
