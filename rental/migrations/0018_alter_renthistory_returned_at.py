# Generated by Django 4.1.7 on 2023-02-26 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rental", "0017_renthistory_returned_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="renthistory",
            name="returned_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
