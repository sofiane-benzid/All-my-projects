from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.titles , name="title"),
    path("search/", views.search , name="search"),
    path("create/", views.create , name="create"),
    path("random/", views.rndm , name="random"),
    path("edit/", views.edit , name="edit"),
    path("save/", views.save, name="save")

]


