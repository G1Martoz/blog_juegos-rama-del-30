# Generated by Django 4.2.3 on 2023-08-04 06:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 4, 6, 15, 55, 140735, tzinfo=datetime.timezone.utc)),
        ),
    ]
