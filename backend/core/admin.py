from django.contrib import admin
from .models import SpiderTask, Job

@admin.register(SpiderTask)
class SpiderTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'frequency', 'created_by', 'created_at')
    list_filter = ('status', 'frequency')
    search_fields = ('name', 'target_url')

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'salary', 'location', 'source_website', 'created_at')
    list_filter = ('source_website',)
    search_fields = ('title', 'company', 'tags')
