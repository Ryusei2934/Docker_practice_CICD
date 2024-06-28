from django.urls import path
from .views import IndexView, AddView, Update_task_complete, TaskUpdate, DeleteView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("add/", AddView.as_view(), name="add"),
    path('update/<int:pk>/', TaskUpdate.as_view(), name='taskupdate'),
    path("Update_task_complete/", Update_task_complete.as_view(), name="Update_task_complete"),
    path("delete/", DeleteView.as_view(), name="delete")
]
