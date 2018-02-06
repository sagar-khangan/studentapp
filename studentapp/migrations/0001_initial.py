# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('maths_score', models.IntegerField(max_length=3)),
                ('science_score', models.IntegerField(max_length=3)),
                ('history_score', models.IntegerField(max_length=3)),
                ('social_score', models.IntegerField(max_length=3)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
