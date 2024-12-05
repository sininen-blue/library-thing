from django.shortcuts import render


def index(request):
    return render(request, "shelves/index.html")


def library(request, lib_name):
    return render(request, "shelves/library.html")


def shelf(request, lib_name, shelf):
    return render(request, "shelves/shelf.html")


def row(request, lib_name, shelf, row):
    return render(request, "shelves/shelf.html")
