# Generated by Django 4.2.6 on 2023-10-25 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookfinds', '0004_alter_book_isbn'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
            ],
        ),
    ]
