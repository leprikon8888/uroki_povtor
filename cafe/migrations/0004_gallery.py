# Generated by Django 4.2.6 on 2023-10-07 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0003_alter_dishcategory_options_alter_dish_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='gallery/')),
                ('is_visible', models.BooleanField(default=True)),
            ],
        ),
    ]
