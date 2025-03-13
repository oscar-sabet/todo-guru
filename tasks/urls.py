from django.urls import path
from . import views

urlpatterns = [
    # path("", views.task_list, name="task_list"),
    path("tasks/", views.tasks, name="tasks"),
    # path("task_board/", views.task_board, name="task_board"),
]
