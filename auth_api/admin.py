from django.contrib import admin
from . models import menu

# menu Model
@admin.register(menu)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'is_completed', 'date', 'time', 'desc', 'date_created', )
