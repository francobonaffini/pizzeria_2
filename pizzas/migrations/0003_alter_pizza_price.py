# Generated by Django 5.0 on 2023-12-23 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0002_rename_descripcion_pizza_desciption_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
