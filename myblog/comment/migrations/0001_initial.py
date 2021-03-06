# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-08-23 08:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=2000, verbose_name=b'\xe5\x86\x85\xe5\xae\xb9')),
                ('nickname', models.CharField(max_length=50, verbose_name=b'\xe6\x98\xb5\xe7\xa7\xb0')),
                ('website', models.URLField(verbose_name=b'\xe7\xbd\x91\xe7\xab\x99')),
                ('email', models.EmailField(max_length=254, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1')),
                ('status', models.PositiveIntegerField(choices=[(1, b'\xe6\xad\xa3\xe5\xb8\xb8'), (0, b'\xe5\x88\xa0\xe9\x99\xa4')], default=1, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post', verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe7\x9b\xae\xe6\xa0\x87')),
            ],
            options={
                'verbose_name': '\u8bc4\u8bba',
                'verbose_name_plural': '\u8bc4\u8bba',
            },
        ),
    ]
