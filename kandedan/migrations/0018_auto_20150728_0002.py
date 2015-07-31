# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kandedan', '0017_auto_20150728_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='message',
            field=models.CharField(default=b'', max_length=1000),
        ),
    ]
