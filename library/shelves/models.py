from django.db import models


class Library(models.Model):
    title = models.CharField(max_length=50, default="")
    description = models.TextField(default="")

    def __str__(self):
        return f"{self.title}"


class Shelf(models.Model):
    library = models.ForeignKey(Library, on_delete=models.CASCADE)

    number = models.IntegerField()
    title = models.CharField(max_length=200, default="None")

    def __str__(self):
        return f"{self.library.title} Shelf {self.number}"


class Row(models.Model):
    shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE)

    number = models.IntegerField()

    def __str__(self):
        return f"Shelf {self.shelf.number} Row {self.number}"


class Book(models.Model):
    row = models.ForeignKey(Row, on_delete=models.SET_NULL, null=True)

    title = models.CharField(max_length=200, default="None")
    author = models.CharField(max_length=200, default="None")
    call_number = models.CharField(max_length=200, default="None")
    barcode = models.CharField(max_length=200, default="None")

    def __str__(self):
        return f"{self.title}"
