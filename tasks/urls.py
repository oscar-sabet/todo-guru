from django.urls import path
from . import views

urlpatterns = [
    path("list/", views.list, name="list"),
    path("create_task/", views.create_task, name="create_task"),
    path("board/", views.board, name="board"),
    path("update_task/<int:task_id>/", views.update_task, name="update_task"),
    path("delete_task/<int:task_id>/", views.delete_task, name="delete_task"),
    path(
        "complete_task/<int:task_id>/",
        views.complete_task,
        name="complete_task"
        ),
    path("profile/", views.profile, name="profile"),
    path(
        "update_task_status/<int:task_id>/",
        views.update_task_status,
        name="update_task_status",
    ),
]
