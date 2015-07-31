# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kandedan', '0005_auto_20150727_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groups',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='trans_detail',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
