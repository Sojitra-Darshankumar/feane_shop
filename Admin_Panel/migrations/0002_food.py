# Generated by Django 4.2 on 2023-07-18 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_Panel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=300)),
                ('price', models.IntegerField()),
                ('photo', models.FileField(default='', upload_to='')),
                ('admin_id', models.BigIntegerField()),
                ('food_category', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Admin_Panel.food_category')),
            ],
        ),
    ]
