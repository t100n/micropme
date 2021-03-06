# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-21 03:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_date', models.DateField(blank=True, null=True)),
                ('country', models.TextField(help_text='Country', max_length=1000)),
                ('file', models.FileField(upload_to='uploads/%Y/%m/%d/')),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id', 'document_date'],
            },
        ),
    ]
