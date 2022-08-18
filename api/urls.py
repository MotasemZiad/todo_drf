from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name='api-overview'),
    path('task-list/', views.task_list, name='task-list'),
    path('task-detail/<int:id>/', views.task_detail, name='task-detail'),
    path('task-create/', views.task_create, name='task-create'),
    path('task-update/<int:id>/', views.task_update, name='task-update'),
    path('task-delete/<int:id>/', views.task_delete, name='task-delete'),
]
