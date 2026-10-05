from django.contrib import admin


from django.contrib import admin
from .models import TodoList


class TodoListAdmin(admin.ModelAdmin):

    list_display = ('title', 'content', 'status', 'created_at')
    
   
    list_display_links = ('title',)
    
   
    search_fields = ('title', 'content')
    
    
    list_filter = ('status', 'created_at')
    
    
    list_editable = ('status',)


admin.site.register(TodoList, TodoListAdmin)
