from django.shortcuts import render
from .models import Library, Shelf, Row, Book
import base64
from io import BytesIO
import qrcode


def index(request):
    libraries = Library.objects.all()

    context = {"libraries": libraries}
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

    qr = qrcode.QRCode()
    qr.add_data(request.get_host() + request.path)
    qrImg = qr.make_image(fill_color=(255, 255, 255),
                          back_color=(12, 113, 195))
    buffer = BytesIO()
    qrImg.save(buffer, format="PNG")
    buffer.seek(0)
    qr64 = base64.b64encode(buffer.getvalue()).decode("utf-8")

    context = {
        "qr": qr64,
        "libraries": libraries,
        "library": library,
        "shelf": shelf,
        "rows": rows,
        "row": row,
        "books": books,
    }
    return render(request, "shelves/shelf.html", context)
