from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/add/', views.add_task, name='add_task'),
    path('tasks/toggle/<int:pk>/', views.toggle_task, name='toggle_task'),
    path('tasks/delete/<int:pk>/', views.delete_task, name='delete_task'),
]
