from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'completed')
    exclude = ('created_at',)


admin.site.register(Task, TaskAdmin)
