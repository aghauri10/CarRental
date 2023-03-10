# Generated by Django 4.1.7 on 2023-02-26 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rental", "0019_rename_car_id_reviews_car_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reviews",
            name="rating",
            field=models.IntegerField(
                choices=[
                    (0.0, "0.0"),
                    (1.0, "1.0"),
                    (2.0, "2.0"),
                    (3.0, "3.0"),
                    (4.0, "4.0"),
                    (5.0, "5.0"),
                ]
            ),
        ),
    ]
