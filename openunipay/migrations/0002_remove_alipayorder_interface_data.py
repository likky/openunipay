# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-18 23:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openunipay', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alipayorder',
            name='interface_data',
        ),
    ]
