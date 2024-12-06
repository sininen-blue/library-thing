from django.urls import path
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import admin
import csv

from .models import Library, Book, Shelf, Row


class BookAdmin(admin.ModelAdmin):
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                "import-csv/",
                self.admin_site.admin_view(self.import_csv),
                name="import_csv",
            ),
        ]
        return custom_urls + urls

    def import_csv(self, request):
        if request.method == "POST" and request.FILES["csv_file"]:
            row_id = request.POST["row"]
            csv_file = request.FILES["csv_file"]
            decoded_file = csv_file.read().decode("utf-8").splitlines()
            reader = csv.DictReader(decoded_file)

            for row in reader:
                Book.objects.create(
                    row=Row.objects.get(pk=row_id),
                    position=row["position"],
                    title=row["title"],
                    author=row["author"],
                    call_number=row["call no"],
                    barcode=row["barcode"],
                )
            messages.success(request, "CSV file imported successfully.")
            return redirect("..")

        context = {"rows": Row.objects.all()}

        return render(request, "admin/csv_import_form.html", context)


admin.site.register(Library)
admin.site.register(Book, BookAdmin)
admin.site.register(Shelf)
admin.site.register(Row)
