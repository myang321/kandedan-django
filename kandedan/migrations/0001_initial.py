# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('creditor', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('debtor', models.CharField(max_length=30)),
                ('amount', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('holder', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Trans_detail',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('debtor', models.CharField(max_length=30)),
                ('amount', models.DecimalField(max_digits=10, decimal_places=2)),
                ('percent', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('username', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=30)),
                ('message', models.CharField(max_length=1000)),
                ('amount', models.DecimalField(max_digits=10, decimal_places=2)),
                ('date', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('username', models.CharField(unique=True, max_length=30)),
                ('password', models.CharField(max_length=50)),
                ('screen_name', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=30)),
                ('group_id', models.ForeignKey(to='kandedan.Groups')),
            ],
        ),
        migrations.AddField(
            model_name='trans_detail',
            name='trans_id',
            field=models.ForeignKey(to='kandedan.Transaction'),
        ),
        migrations.AlterUniqueTogether(
            name='balance',
            unique_together=set([('creditor', 'debtor')]),
        ),
    ]
