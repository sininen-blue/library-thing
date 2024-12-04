from django.db import models


class Shelf(models.Model):
    title = models.CharField(max_length=200)


class Book(models.Model):
    shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
