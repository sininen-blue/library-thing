from django.contrib import admin

from .models import Library, Book, Shelf, Row

admin.site.register(Library)
admin.site.register(Book)
admin.site.register(Shelf)
admin.site.register(Row)
