from django.urls import path

from problems import views


app_name = "problems"

urlpatterns = [
    path("", views.problems, name="index"),
    path("about_problems/", views.about_problems, name="about_problems")
]