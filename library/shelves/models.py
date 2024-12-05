from django.db import models


class Library(models.Model):
    title = models.CharField(max_length=50, default="")


class Shelf(models.Model):
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)


class Book(models.Model):
    shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
