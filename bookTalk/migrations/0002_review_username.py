# Generated by Django 4.2.6 on 2023-10-29 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookTalk', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='username',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]