# Generated by Django 3.2.8 on 2021-10-11 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookHub_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='author',
            new_name='uploader',
        ),
        migrations.RemoveField(
            model_name='books',
            name='name',
        ),
        migrations.RemoveField(
            model_name='books',
            name='upload_time',
        ),
        migrations.RemoveField(
            model_name='books',
            name='writer_name',
        ),
        migrations.AddField(
            model_name='books',
            name='author_name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='books',
            name='book_name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='books',
            name='uploaded_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]