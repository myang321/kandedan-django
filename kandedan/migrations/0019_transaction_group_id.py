# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kandedan', '0018_auto_20150728_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='group_id',
            field=models.ForeignKey(default=1, to='kandedan.Groups'),
            preserve_default=False,
        ),
    ]
