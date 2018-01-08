# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-05 04:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0004_auto_20180102_1910'),
        ('courses', '0002_auto_20180105_0413'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='CourseOrg',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.CourseOrg', verbose_name='courseOrg'),
        ),
    ]