# Generated by Django 5.0 on 2023-12-23 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=5)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='C:\\Users\\codig\\Desktop\\drf-pizza\\pizza_project\\pizzas\\media\\img')),
            ],
        ),
    ]