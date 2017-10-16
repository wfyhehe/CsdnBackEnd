#!/usr/bin/env python
# -*- coding: utf-8 -*-
import django_filters

from csdn.models import CsdnArticle, CsdnAuthor

__author__ = 'wfy'
__date__ = '2017/10/14 20:51'


class ArticleFilter(django_filters.rest_framework.FilterSet):
    start_time = django_filters.DateTimeFilter(name='create_date', lookup_expr='gte')
    end_time = django_filters.DateTimeFilter(name='create_date', lookup_expr='lte')
    view_num_min = django_filters.NumberFilter(name='view_num', lookup_expr='gte')
    view_num_max = django_filters.NumberFilter(name='view_num', lookup_expr='lte')
    comment_num_min = django_filters.NumberFilter(name='comment_num', lookup_expr='gte')
    comment_num_max = django_filters.NumberFilter(name='comment_num', lookup_expr='lte')

    class Meta:
        model = CsdnArticle
        fields = ['view_num_min', 'view_num_max', 'comment_num_min', 'comment_num_max',
                  'start_time', 'end_time']


class AuthorFilter(django_filters.rest_framework.FilterSet):
    fans_num_min = django_filters.NumberFilter(name='fans_num', lookup_expr='gte')
    fans_num_max = django_filters.NumberFilter(name='fans_num', lookup_expr='lte')
    focus_num_min = django_filters.NumberFilter(name='focus_num', lookup_expr='gte')
    focus_num_max = django_filters.NumberFilter(name='focus_num', lookup_expr='lte')
    blog_score_min = django_filters.NumberFilter(name='blog_score', lookup_expr='gte')
    blog_score_max = django_filters.NumberFilter(name='blog_score', lookup_expr='lte')

    class Meta:
        model = CsdnAuthor
        fields = ['fans_num_min', 'fans_num_max', 'focus_num_min', 'focus_num_max',
                  'blog_score_min', 'blog_score_max']
