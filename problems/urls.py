from django.urls import path

from problems import views


app_name = "problems"

urlpatterns = [
    path("", views.problems, name="index"),
    path('create/', views.create_problem, name='create_problem'),
    path("about_problems/<int:id>/", views.about_problems, name="about_problems"),
    path('admin/problem/<int:pk>/edit/', views.admin_edit_problem, name='admin_edit_problem'),
    path('admin/category/add/', views.admin_add_category, name='admin_add_category'),

]