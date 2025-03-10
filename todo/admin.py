from django.contrib import admin

from todo.models import TodoList


@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
