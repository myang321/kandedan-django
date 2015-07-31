# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kandedan', '0015_auto_20150727_2352'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='message',
            new_name='message1',
        ),
    ]
