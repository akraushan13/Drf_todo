from django.contrib import admin

# Register your models here.

from .models import Todo


@admin.register(Todo)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'due_date')
