from . import views
from django.urls import path

urlpatterns = [
    path('list/', views.todo, name='todo'),
    path('insert_todo', views.todo_insert, name='insert_todo_item'),
    path('delete_todo/<int:todo_id>/', views.delete_todo_item, name='delete_todo_item'),
]