# Generated by Django 5.0.2 on 2024-02-11 19:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MetaHotel',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('supplier_id', models.CharField(max_length=255)),
                ('meta_hotel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hotels', to='hotels.metahotel')),
            ],
        ),
    ]