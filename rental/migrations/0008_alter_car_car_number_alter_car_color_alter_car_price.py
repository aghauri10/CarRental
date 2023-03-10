# Generated by Django 4.1.7 on 2023-02-19 19:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rental", "0007_alter_car_brand_alter_car_mileage_alter_car_year"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="car_number",
            field=models.CharField(max_length=25, unique=True),
        ),
        migrations.AlterField(
            model_name="car",
            name="color",
            field=models.CharField(
                choices=[
                    ("White", "White"),
                    ("Black", "Black"),
                    ("Grey", "Grey"),
                    ("Silver", "Silver"),
                    ("Blue", "Blue"),
                    ("Red", "Red"),
                    ("Brown", "Brown"),
                    ("Green", "Green"),
                    ("Orange", "Orange"),
                    ("Purple", "Purple"),
                    ("Beige", "Beige"),
                    ("Purple", "Purple"),
                    ("Gold", "Gold"),
                    ("Yellow", "Yellow"),
                ],
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="car",
            name="price",
            field=models.IntegerField(
                validators=[django.core.validators.MinValueValidator(0)]
            ),
        ),
    ]
