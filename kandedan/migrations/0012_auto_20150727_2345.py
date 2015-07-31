# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kandedan', '0011_transaction_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='trans_type',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
