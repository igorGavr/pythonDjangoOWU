# Generated by Django 4.1.3 on 2022-12-12 13:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0002_alter_pizzamodel_imageurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizzamodel',
            name='weight',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pizzamodel',
            name='imageUrl',
            field=models.CharField(max_length=120, unique=True, validators=[django.core.validators.MaxLengthValidator(2), django.core.validators.MaxLengthValidator(120)]),
        ),
    ]
