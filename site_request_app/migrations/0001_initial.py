# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('create_date', models.DateTimeField(verbose_name=b'date created')),
                ('description', models.CharField(max_length=2000)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
    ]
