# Generated by Django 4.0.6 on 2022-08-25 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='latitude',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='position',
            name='longitude',
            field=models.CharField(max_length=20),
        ),
    ]
