from django.contrib import admin
from .models import Category, Thread, Post, Like

admin.site.register(Category)
admin.site.register(Thread)
admin.site.register(Post)
admin.site.register(Like)
