from django.urls import path

from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.main_view, name="main"),
]
