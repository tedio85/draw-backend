# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 08:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_num', models.IntegerField()),
                ('target_text', models.CharField(max_length=200)),
                ('target_img', models.ImageField(upload_to='')),
            ],
        ),
    ]
