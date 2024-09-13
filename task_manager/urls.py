"""
URL configuration for it_company_task_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from task_manager.views import index, TaskTypeListView, PositionListView, WorkerListView, TaskListView, \
    WorkerDetailView, WorkerCreateView, WorkerDeleteView, WorkerUpdateView

urlpatterns = [
    path("", index, name="index"),
    path("task_types/", TaskTypeListView.as_view(), name="task-type-list"),
    path("positions/", PositionListView.as_view(), name="position-list"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("workers/create/", WorkerCreateView.as_view(), name="worker-create"),
    path("workers/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
    path("workers/<int:pk>/update", WorkerUpdateView.as_view(), name="worker-update"),
    path("workers/<int:pk>/delete", WorkerDeleteView.as_view(), name="worker-delete"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
]

app_name = "task_manager"
