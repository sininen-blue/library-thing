from django.urls import path

from . import views

app_name = "shelves"
urlpatterns = [
    path("", views.index, name="index"),
    path("lib/<str:lib_name>", views.library, name="library"),
    path("lib/<str:lib_name>/<int:shelf>", views.shelf, name="shelf"),
    path("lib/<str:lib_name>/<int:shelf>/<int:row>", views.row, name="row"),
]
