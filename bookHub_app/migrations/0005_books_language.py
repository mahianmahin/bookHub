# Generated by Django 3.2.8 on 2021-10-11 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookHub_app', '0004_books_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='language',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]