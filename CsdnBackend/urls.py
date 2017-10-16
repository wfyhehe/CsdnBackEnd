"""CsdnBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.static import serve
from rest_framework.routers import DefaultRouter

from CsdnBackend.settings import MEDIA_ROOT
from csdn.views import AuthorViewSet, ArticleViewSet, home

router = DefaultRouter()

router.register(r'article', ArticleViewSet, base_name='article')
router.register(r'author', AuthorViewSet, base_name='author')

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'^', include(router.urls)),
    # url(r'^article/$', views.ArticleList.as_view()),
    # url(r'^article/(?P<pk>[0-9]+)/$', views.ArticleDetail.as_view()),
]
