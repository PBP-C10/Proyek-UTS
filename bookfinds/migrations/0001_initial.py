# Generated by Django 4.2.6 on 2023-10-13 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.IntegerField()),
                ('title', models.CharField(max_length=255)),
                ('subtitle', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('categories', models.CharField(max_length=255)),
                ('thumbnail', models.URLField()),
                ('description', models.TextField()),
                ('published_year', models.IntegerField(max_length=4)),
                ('average_rating', models.DecimalField(decimal_places=2, max_digits=2)),
                ('num_pages', models.IntegerField()),
                ('ratings_count', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]