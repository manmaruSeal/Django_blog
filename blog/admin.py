from django.contrib import admin
#使用するモデルのインポートを忘れずに
from .models import Post, Comment

admin.site.register(Post)
admin.site.register(Comment)