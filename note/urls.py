from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    # This single path connects to the todo_manager function for BOTH requests!
    path('admin/', admin.site.urls),
    path('todos/', views.todo_manager, name='todo_view'),
    path('todos/update/<int:pk>/', views.update_todo, name='update_view'),
    path('todos/delete/<int:pk>/', views.delete_todo, name='delete_view'),
]
