# Generated by Django 4.1.7 on 2023-02-19 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rental", "0008_alter_car_car_number_alter_car_color_alter_car_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="car",
            name="dscription",
            field=models.CharField(default="good", max_length=1000),
            preserve_default=False,
        ),
    ]
