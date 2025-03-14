from django.urls import path
from . import views

urlpatterns = [
    # path("", views.task_list, name="task_list"),
    path("tasks/", views.tasks, name="tasks"),
    # path("task_board/", views.task_board, name="task_board"),
    path("create_task/", views.create_task, name="create_task"),
    # path(
    #     "update_task_status/<int:task_id>/",
    #     views.update_task_status,
    #     name="update_task_status",
    # ),
    path("update_task/<int:task_id>/", views.update_task, name="update_task"),
    path("delete_task/<int:task_id>/", views.delete_task, name="delete_task"),
]
