# Generated by Django 5.0.2 on 2024-06-12 08:28

import django.contrib.postgres.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParkingPlace',
            fields=[
                ('_id', models.CharField(primary_key=True, serialize=False)),
                ('coordinates', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None), size=None)),
                ('floor', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FacilityType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Elevator', 'Лифт'), ('Escalator', 'Эскалатор'), ('Entrance', 'Вход')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('_id', models.CharField(primary_key=True, serialize=False)),
                ('slug', models.CharField(max_length=100)),
                ('coordinates', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None), size=None)),
                ('category', models.CharField(max_length=100)),
                ('floor', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Busy',
            fields=[
                ('_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='busy_set', serialize=False, to='parkings.parkingplace')),
                ('is_busy', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('_id', models.CharField(primary_key=True, serialize=False)),
                ('floor', models.IntegerField()),
                ('coordinates', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None), size=None)),
                ('slug', models.CharField(max_length=100)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='facilityType_set', to='parkings.facilitytype')),
            ],
        ),
        migrations.CreateModel(
            name='Path',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('path_coordinates', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.DecimalField(decimal_places=2, max_digits=10), size=None), size=None)),
                ('place_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='path_set', to='parkings.parkingplace')),
                ('shop_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='path_set', to='parkings.shop')),
            ],
        ),
    ]
