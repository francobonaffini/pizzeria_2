# Generated by Django 5.0 on 2024-03-09 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0003_alter_pizza_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img/pizzas/'),
        ),
    ]