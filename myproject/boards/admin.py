from django.contrib import admin

from .models import Board, Post, Topic

class TopicDate(admin.ModelAdmin):
    readonly_fields = ['created_at']
class PostDate(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')


admin.site.register(Board)
admin.site.register(Topic,TopicDate)
admin.site.register(Post, PostDate)

