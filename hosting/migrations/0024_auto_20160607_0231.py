# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-07 02:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosting', '0023_virtualmachineplan_configutarion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='virtualmachineplan',
            old_name='configutarion',
            new_name='configuration',
        ),
    ]