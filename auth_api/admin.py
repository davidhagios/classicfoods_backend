from django.contrib import admin
from . models import Task

# Task Model
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'is_completed', 'date', 'time', 'desc', 'date_created', )
