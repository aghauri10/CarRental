# Generated by Django 4.1.7 on 2023-02-26 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rental", "0016_alter_car_description_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="renthistory",
            name="returned_at",
            field=models.DateTimeField(blank=True, default=None),
            preserve_default=False,
        ),
    ]