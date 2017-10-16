#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import serializers

from csdn.models import CsdnArticle, CsdnAuthor

__author__ = 'wfy'
__date__ = '2017/10/14 18:50'


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CsdnArticle
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CsdnAuthor
        fields = '__all__'
