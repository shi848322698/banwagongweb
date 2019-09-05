from django.contrib import admin
from .models import ArticleColumn, ArticlePost


class ArticleColumnAdmin(admin.ModelAdmin):
    list_display = ('column', 'created', 'user')
    list_filter = ("column",)

class ArticlePOSTAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'created')
    list_filter = ("author",)

admin.site.register(ArticleColumn, ArticleColumnAdmin)
admin.site.register(ArticlePost, ArticlePOSTAdmin)


# Register your models here.
