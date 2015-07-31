# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kandedan', '0016_auto_20150727_2354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='message1',
        ),
        migrations.AddField(
            model_name='transaction',
            name='message',
            field=models.CharField(default=b'', max_length=1000, null=True),
        ),
    ]
