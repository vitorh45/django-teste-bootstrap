from django.contrib import admin
from .models import Category, Post

class CategoryAdmin(admin.ModelAdmin):
	pass

class PostAdmin(admin.ModelAdmin):
	list_display = ['title']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)