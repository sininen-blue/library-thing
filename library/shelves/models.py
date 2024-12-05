from django.db import models


class Library(models.Model):
    title = models.CharField(max_length=50, default="")

    def __str__(self):
        return f"{self.title}"


class Shelf(models.Model):
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    number = models.IntegerField(default=0)
    title = models.CharField(max_length=200, default="")


class Book(models.Model):
    shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    call_number = models.CharField(max_length=200)
    barcode = models.CharField(max_length=200)
