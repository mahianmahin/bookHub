# Generated by Django 3.2.8 on 2021-10-12 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookHub_app', '0016_alter_books_book_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='book_rating',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True),
        ),
    ]
