# Generated by Django 4.2.6 on 2023-10-07 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0002_dish'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dishcategory',
            options={'ordering': ('position',)},
        ),
        migrations.AlterField(
            model_name='dish',
            name='position',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
