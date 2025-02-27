from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    # Basically, servers as index file.
    path('task_create/', views.task_create, name='task_create'), 
    path('submit/', views.submit),
    # For adding a new task with the submit function.
    path('task_update/<int:task_id>', views.task_update, name='task_update'),
    path('task_update/update/', views.update, name='update'),
    # For updating an existing task.
    path('task_delete/<int:task_id>', views.task_delete, name='task_delete'),
    path('task_delete/delete/', views.delete, name='delete'),
    # For deleting an existing task.
]


