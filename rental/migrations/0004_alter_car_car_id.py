# Generated by Django 4.1.7 on 2023-02-18 13:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("rental", "0003_alter_customer_occupation"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="car_id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
    ]
