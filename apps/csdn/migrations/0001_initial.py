# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CsdnArticle',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=300)),
                ('url_object_id', models.CharField(max_length=32, serialize=False, primary_key=True)),
                ('author', models.CharField(max_length=64)),
                ('view_num', models.IntegerField()),
                ('comment_num', models.IntegerField()),
                ('like_num', models.IntegerField(null=True, blank=True)),
                ('dig_num', models.IntegerField(null=True, blank=True)),
                ('bury_num', models.IntegerField(null=True, blank=True)),
                ('create_date', models.DateTimeField(null=True, blank=True)),
                ('crawl_date', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'csdn_article',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CsdnAuthor',
            fields=[
                ('url', models.CharField(max_length=300)),
                ('url_object_id', models.CharField(max_length=32, serialize=False, primary_key=True)),
                ('avatar_url', models.CharField(max_length=300, null=True, blank=True)),
                ('avatar_path', models.CharField(max_length=200, null=True, blank=True)),
                ('username', models.CharField(max_length=64)),
                ('nick_name', models.CharField(max_length=64)),
                ('detail', models.CharField(max_length=300, null=True, blank=True)),
                ('sign', models.CharField(max_length=300, null=True, blank=True)),
                ('blog_score', models.IntegerField()),
                ('download_score', models.IntegerField()),
                ('bbs_score', models.IntegerField()),
                ('code_score', models.IntegerField()),
                ('focus_num', models.IntegerField()),
                ('fans_num', models.IntegerField()),
                ('crawl_date', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'csdn_author',
                'managed': True,
            },
        ),
    ]
