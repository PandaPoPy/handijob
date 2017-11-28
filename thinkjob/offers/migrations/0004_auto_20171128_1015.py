# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 10:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0003_auto_20171128_0949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appliance',
            name='candidate_user',
        ),
        migrations.RemoveField(
            model_name='appliance',
            name='offer',
        ),
        migrations.AlterField(
            model_name='enterprise',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='enterprise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offers.Enterprise'),
        ),
        migrations.DeleteModel(
            name='Appliance',
        ),
    ]
