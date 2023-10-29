# Generated by Django 4.2.6 on 2023-10-28 16:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bookfinds', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('books', models.ManyToManyField(related_name='carts', to='bookfinds.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.IntegerField(choices=[(1, 'Transfer Bank'), (2, 'Gopay'), (3, 'OVO')])),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(max_length=254)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='BookShop.cart')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
