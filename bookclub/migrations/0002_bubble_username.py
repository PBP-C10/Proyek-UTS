# Generated by Django 4.2.6 on 2023-11-20 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookclub', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bubble',
            name='username',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
