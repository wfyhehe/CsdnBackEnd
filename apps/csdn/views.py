import json

from django.forms import model_to_dict
from django.http import Http404
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, render_to_response

# Create your views here.
from django.views.generic import View
from django.core import serializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import mixins
from rest_framework import status
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from csdn.fiilters import ArticleFilter, AuthorFilter
from csdn.models import CsdnArticle, CsdnAuthor
from csdn.serializers import ArticleSerializer, AuthorSerializer


class ArticlePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'page_index'
    max_page_size = 100


class ArticleViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = CsdnArticle.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = ArticlePagination
    filter_backends = {DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter}
    filter_class = ArticleFilter
    search_fields = {'title', 'author'}
    ordering_field = {'view_num', 'comment_num', 'create_date'}


class AuthorPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'page_index'
    max_page_size = 100


class AuthorViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = CsdnAuthor.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = AuthorPagination
    filter_backends = {DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter}
    filter_class = AuthorFilter
    search_fields = {'detail', 'nick_name'}
    ordering_field = {'focus_num', 'fans_num', 'blog_score'}


def home(request):
    response = render_to_response('index.html')
    return response
