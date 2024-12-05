from django.urls import path

from . import views

app_name = "shelves"
urlpatterns = [
    path("", views.index, name="index"),
    path("lib/<int:lib_id>", views.library, name="library"),
    path("lib/<int:lib_id>/<int:shelf>", views.shelf, name="shelf"),
    path("lib/<int:lib_id>/<int:shelf>/<int:row>", views.row, name="row"),
]
