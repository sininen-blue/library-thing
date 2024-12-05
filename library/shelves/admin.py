from django.contrib import admin

from .models import Library, Book, Shelf

admin.site.register(Library)
admin.site.register(Book)
admin.site.register(Shelf)
