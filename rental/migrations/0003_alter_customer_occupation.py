# Generated by Django 4.1.7 on 2023-02-18 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rental", "0002_customer_alter_reviews_user_id_delete_userx"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="occupation",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Student", "Student"),
                    ("Unemployed", "Unemployed"),
                    ("Employed", "Employed"),
                ],
                default="Unemployed",
                max_length=50,
            ),
        ),
    ]