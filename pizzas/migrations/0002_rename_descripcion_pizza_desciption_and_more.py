# Generated by Django 5.0 on 2023-12-23 22:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pizza',
            old_name='descripcion',
            new_name='desciption',
        ),
        migrations.RenameField(
            model_name='pizza',
            old_name='imagen',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='pizza',
            old_name='nombre',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='pizza',
            old_name='precio',
            new_name='price',
        ),
    ]
