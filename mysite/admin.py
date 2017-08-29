from django.contrib import admin
from mysite.models import Mood, Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
	list_display = ('nickname', 'message', 'enabled', 'pub_time')
	ordering = ('-pub_time',)

admin.site.register(Mood)
admin.site.register(Post, PostAdmin)
