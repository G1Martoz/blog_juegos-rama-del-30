# Generated by Django 4.2.3 on 2023-08-04 06:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contacto', '0002_alter_contacto_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
