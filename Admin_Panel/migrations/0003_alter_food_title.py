# Generated by Django 4.2 on 2023-07-18 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_Panel', '0002_food'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]
