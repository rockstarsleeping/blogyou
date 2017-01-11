from django.contrib import admin
from blog.models import Article
from django.contrib.auth.models import User

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'decription', 'likes', 'views')

admin.site.register(Article)
