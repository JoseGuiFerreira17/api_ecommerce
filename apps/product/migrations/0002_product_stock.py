# Generated by Django 5.0.3 on 2024-03-12 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="stock",
            field=models.PositiveIntegerField(
                default=0, verbose_name="quantidade em estoque"
            ),
        ),
    ]
