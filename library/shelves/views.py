from django.shortcuts import render
from .models import Library, Shelf, Row, Book


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


def shelf(request, lib_id, shelf_id):
    libraries = Library.objects.all()
    library = libraries.get(pk=lib_id)
    shelf = Shelf.objects.get(pk=shelf_id)
    rows = Row.objects.filter(shelf=shelf)

    context = {
        "libraries": libraries,
        "library": library,
        "shelf": shelf,
        "rows": rows,
    }
    return render(request, "shelves/shelf.html", context)


def row(request, lib_id, shelf_id, row_id):
    libraries = Library.objects.all()
    library = libraries.get(pk=lib_id)
    shelf = Shelf.objects.get(pk=shelf_id)
    rows = Row.objects.filter(shelf=shelf)
    row = Row.objects.get(pk=row_id)
    books = Book.objects.filter(row=row)

    context = {
        "libraries": libraries,
        "library": library,
        "shelf": shelf,
        "rows": rows,
        "row": row,
        "books": books,
    }
    return render(request, "shelves/shelf.html", context)
