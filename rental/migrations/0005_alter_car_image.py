# Generated by Django 4.1.7 on 2023-02-18 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rental", "0004_alter_car_car_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="image",
            field=models.ImageField(upload_to="images/car/"),
        ),
    ]
