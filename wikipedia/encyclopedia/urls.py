from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>", views.description, name="description"),
    path("search/", views.search, name="search"),
    path("newpage/", views.newpage, name="newpage"),
    path("edit/<str:name>", views.edit, name = "edit"),
    path("save_edit/<str:name>", views.save_edit, name = "save_edit"),
    path("random_page/", views.random_page, name = "random_page")
]
