# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 08:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TheWall', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
        migrations.RenameModel(
            old_name='Messages',
            new_name='Message',
        ),
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
    ]