from django.urls import path

from . import views

app_name = "shelves"
urlpatterns = [
    path("", views.index, name="index"),
    path("lib/<int:lib_id>", views.library, name="library"),
    path("lib/<int:lib_id>/<int:shelf_id>", views.shelf, name="shelf"),
    path("lib/<int:lib_id>/<int:shelf_id>/<int:row_id>", views.row, name="row"),
]
