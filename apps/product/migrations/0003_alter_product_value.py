# Generated by Django 5.1.6 on 2025-02-20 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0002_product_stock"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="value",
            field=models.DecimalField(
                decimal_places=2, max_digits=10, verbose_name="valor"
            ),
        ),
    ]
