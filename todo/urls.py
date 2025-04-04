from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/add/', views.add_task, name='add_task'),
    path('tasks/<int:pk>/toggle/', views.toggle_task, name='toggle_task'),
    path('tasks/<int:pk>/delete/', views.delete_task, name='delete_task'),
    path('', views.task_list),  # This maps the base `/todo/` URL to the task list view
]
