# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kandedan', '0006_auto_20150727_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groups',
            name='holder',
            field=models.ForeignKey(to='kandedan.Users'),
        ),
        migrations.AlterField(
            model_name='trans_detail',
            name='debtor',
            field=models.ForeignKey(to='kandedan.Users'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='username',
            field=models.ForeignKey(to='kandedan.Users'),
        ),
    ]
