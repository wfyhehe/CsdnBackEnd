from django.contrib import admin

# Register your models here.
from csdn.models import CsdnArticle, CsdnAuthor


class ArticleAdmin(admin.ModelAdmin):
    fields = '__all__'


class AuthorAdmin(admin.ModelAdmin):
    fields = '__all__'


admin.site.register(CsdnArticle)
admin.site.register(CsdnAuthor)
