# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kandedan', '0008_auto_20150727_1607'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trans_detail',
            old_name='trans_id',
            new_name='trans',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='username',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='group_id',
            new_name='group',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.CharField(default=b'', max_length=30),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='message',
            field=models.CharField(default=b'', max_length=1000),
        ),
    ]
