# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(null=True, blank=True)),
                ('polarity', models.DecimalField(null=True, max_digits=25, decimal_places=20, blank=True)),
                ('subjectivity', models.DecimalField(null=True, max_digits=25, decimal_places=20, blank=True)),
                ('movie', models.ForeignKey(to='movie.Movie', null=True)),
            ],
        ),
    ]
