# Generated by Django 4.0.6 on 2022-10-11 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='content',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='notification',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
