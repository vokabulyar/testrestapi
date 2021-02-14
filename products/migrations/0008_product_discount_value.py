# Generated by Django 3.2a1 on 2021-02-14 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_remove_product_discount_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount_value',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='products.discount', verbose_name='Скидка в процентах'),
        ),
    ]