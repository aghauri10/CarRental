# Generated by Django 4.1.6 on 2023-02-16 14:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rental', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('X', 'Prefer Not to Say')], max_length=50)),
                ('dob', models.DateField()),
                ('occupation', models.CharField(blank=True, choices=[('Student', 'Student'), ('Unemployed', 'Unemployed'), ('Employed', 'Unemployed')], default='Unemployed', max_length=50)),
                ('phone_number', models.CharField(max_length=15)),
                ('license_number', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='reviews',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental.customer'),
        ),
        migrations.DeleteModel(
            name='UserX',
        ),
    ]