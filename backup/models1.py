# coding=utf-8
from __future__ import unicode_literals
from django.db import models


# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='文章标题')
    url = models.CharField(max_length=300, verbose_name='url')
    url_object_id = models.CharField(max_length=32, verbose_name='url的MD5(主键)')
    author = models.CharField(max_length=64, verbose_name='作者用户名')
    view_num = models.IntegerField(default=0, verbose_name='阅读次数')
    comment_num = models.IntegerField(default=0, verbose_name='评论次数')
    like_num = models.IntegerField(null=True, verbose_name='收藏次数')
    dig_num = models.IntegerField(null=True, verbose_name='顶次数')
    bury_num = models.IntegerField(null=True, verbose_name='踩次数')
    create_date = models.DateTimeField(null=True, verbose_name='发表时间')
    crawl_date = models.DateTimeField(null=True, verbose_name='爬取时间')

    class Meta:
        verbose_name = u'CSDN博客文章'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title


class Author(models.Model):
    url = models.CharField(max_length=300, verbose_name='url')
    url_object_id = models.CharField(max_length=32, verbose_name='url的MD5(主键)')
    avatar_url = models.CharField(null=True, max_length=300, verbose_name='头像url')
    avatar_path = models.CharField(null=True, max_length=32, verbose_name='头像本地路径')
    username = models.CharField(max_length=64, verbose_name='用户名')
    nick_name = models.CharField(max_length=64, verbose_name='昵称')
    detail = models.CharField(null=True, max_length=300, verbose_name='个人描述')
    sign = models.CharField(null=True, max_length=300, verbose_name='个性签名')
    blog_score = models.IntegerField(default=0, verbose_name='博客积分')
    download_score = models.IntegerField(default=0, verbose_name='下载积分')
    bbs_score = models.IntegerField(default=0, verbose_name='论坛积分')
    code_score = models.IntegerField(default=0, verbose_name='代码积分')
    focus_num = models.IntegerField(default=0, verbose_name='关注数')
    fans_num = models.IntegerField(default=0, verbose_name='粉丝数')
    crawl_date = models.DateTimeField(null=True, verbose_name='爬取时间')

    class Meta:
        verbose_name = u'CSDN博主'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username
