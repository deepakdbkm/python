# Generated by Django 3.1.8 on 2021-06-09 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo1app', '0005_place_non'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='place1',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
