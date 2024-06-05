# Generated by Django 5.0.6 on 2024-05-27 17:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, validators=[django.core.validators.RegexValidator(message='Email must be a valid KNUST student email', regex='^[a-zA-Z0-9._%+-]+@st\\.knust\\.edu\\.gh$')])),
                ('phone_number', models.CharField(max_length=15)),
                ('booking_date', models.DateField()),
                ('message', models.TextField()),
            ],
        ),
    ]
