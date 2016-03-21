# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-20 20:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('narratives', '0003_auto_20160320_2050'),
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='narratives.Narrative'),
        ),
    ]
