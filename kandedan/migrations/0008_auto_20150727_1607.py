# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kandedan', '0007_auto_20150727_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trans_detail',
            name='percent',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='message',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='group_id',
            field=models.ForeignKey(to='kandedan.Groups', null=True),
        ),
    ]
