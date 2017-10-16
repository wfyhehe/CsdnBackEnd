# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class CsdnArticle(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=300)
    url_object_id = models.CharField(primary_key=True, max_length=32)
    author = models.CharField(max_length=64)
    view_num = models.IntegerField()
    comment_num = models.IntegerField()
    like_num = models.IntegerField(blank=True, null=True)
    dig_num = models.IntegerField(blank=True, null=True)
    bury_num = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    crawl_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'csdn_article'

    def __unicode__(self):
        return self.title


class CsdnAuthor(models.Model):
    url = models.CharField(max_length=300)
    url_object_id = models.CharField(primary_key=True, max_length=32)
    avatar_url = models.CharField(max_length=300, blank=True, null=True)
    avatar_path = models.CharField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=64)
    nick_name = models.CharField(max_length=64)
    detail = models.CharField(max_length=300, blank=True, null=True)
    sign = models.CharField(max_length=300, blank=True, null=True)
    blog_score = models.IntegerField()
    download_score = models.IntegerField()
    bbs_score = models.IntegerField()
    code_score = models.IntegerField()
    focus_num = models.IntegerField()
    fans_num = models.IntegerField()
    crawl_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'csdn_author'

    def __unicode__(self):
        return self.username
