from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('addTask', views.addTask),
    path('editTask/<int:task_id>', views.editTask),
    path('editTask/update/', views.update),
    path('deleteTask/<int:task_id>', views.deleteTask),
    path('deleteTask/delete/', views.delete),
    
    path('submit/', views.submit),
]

