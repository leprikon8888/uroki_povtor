# Generated by Django 4.2.6 on 2023-10-08 10:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0004_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the format: +38(0xx)xxxxxxx', regex='^[\\+]?[(]?[0-9]{3}[)]?[-\\s\\.]?[0-9]{3}[-\\s\\.]?[0-9]{4,6}$')])),
                ('date', models.DateField()),
                ('time', models.TextField()),
                ('people', models.PositiveSmallIntegerField()),
                ('message', models.TextField(blank=True, max_length=200)),
                ('is_processed', models.BooleanField(default=False)),
                ('date_in', models.DateTimeField(auto_now_add=True)),
                ('date_modify', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
    ]
