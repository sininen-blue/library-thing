from django.shortcuts import render
from .models import Library, Shelf, Book


def index(request):
    libraries = Library.objects.all()

    context = {
        "libraries": libraries
    }
    return render(request, "shelves/index.html", context)


def library(request, lib_id):
    libraries = Library.objects.all()
    library = libraries.get(pk=lib_id)
    shelves = Shelf.objects.filter(library=library).order_by("number")

    context = {
        "libraries": libraries,
        "library": library,
        "shelves": shelves,
    }
    return render(request, "shelves/library.html", context)


def shelf(request, lib_id, shelf):
    return render(request, "shelves/shelf.html")


def row(request, lib_id, shelf, row):
    return render(request, "shelves/shelf.html")
