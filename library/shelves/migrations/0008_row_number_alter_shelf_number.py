# Generated by Django 5.1.3 on 2024-12-05 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelves', '0007_remove_book_shelf_row_book_row'),
    ]

    operations = [
        migrations.AddField(
            model_name='row',
            name='number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shelf',
            name='number',
            field=models.IntegerField(),
        ),
    ]