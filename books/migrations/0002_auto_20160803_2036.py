# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-03 20:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='cover_img',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='purchase_link',
            new_name='link',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='publication_date',
            new_name='publish_date',
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.CharField(max_length=150),
        ),
    ]
