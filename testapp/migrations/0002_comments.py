# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-24 10:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=250)),
                ('commentor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.Authors')),
            ],
        ),
    ]