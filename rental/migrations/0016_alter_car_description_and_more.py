# Generated by Django 4.1.7 on 2023-02-25 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rental", "0015_car_is_available"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="description",
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name="renthistory",
            name="damage_description",
            field=models.TextField(default="To be filled by system when car returned"),
        ),
    ]
