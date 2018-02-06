# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='history_score',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='maths_score',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='science_score',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='social_score',
            field=models.IntegerField(),
        ),
    ]
