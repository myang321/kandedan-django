# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kandedan', '0014_auto_20150727_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groups',
            name='holder',
            field=models.ForeignKey(default=1, to='kandedan.Users'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='trans_detail',
            name='debtor',
            field=models.ForeignKey(default=1, to='kandedan.Users'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='trans_detail',
            name='trans',
            field=models.ForeignKey(default=1, to='kandedan.Transaction'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='users',
            name='user_type',
            field=models.CharField(default=b'normal', max_length=30),
        ),
    ]
