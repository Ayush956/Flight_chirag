# Generated by Django 4.1.5 on 2023-06-18 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_alter_mybookings_data_flight_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mybookings_data',
            name='flight_time_arrival',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='mybookings_data',
            name='flight_time_depart',
            field=models.CharField(max_length=200),
        ),
    ]
