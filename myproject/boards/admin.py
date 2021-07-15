from django.contrib import admin

from .models import Board, Company, Topic, Employee

class TopicDate(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')


admin.site.register(Board)
admin.site.register(Topic,TopicDate)
admin.site.register(Company)
admin.site.register(Employee)

