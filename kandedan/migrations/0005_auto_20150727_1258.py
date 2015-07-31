# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kandedan', '0004_auto_20150727_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='uid',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
