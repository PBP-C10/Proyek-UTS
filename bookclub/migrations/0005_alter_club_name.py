# Generated by Django 4.2.6 on 2023-10-26 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookclub', '0004_bubble_club'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
