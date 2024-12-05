# Generated by Django 5.1.3 on 2024-12-05 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelves', '0004_book_author_book_barcode_book_call_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(default='None', max_length=200),
        ),
        migrations.AlterField(
            model_name='book',
            name='barcode',
            field=models.CharField(default='None', max_length=200),
        ),
        migrations.AlterField(
            model_name='book',
            name='call_number',
            field=models.CharField(default='None', max_length=200),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(default='None', max_length=200),
        ),
        migrations.AlterField(
            model_name='shelf',
            name='title',
            field=models.CharField(default=' ', max_length=200),
        ),
    ]