# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kandedan', '0012_auto_20150727_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='trans_type',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
