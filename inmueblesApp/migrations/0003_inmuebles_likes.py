# Generated by Django 3.2.8 on 2021-11-24 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmueblesApp', '0002_imageninmuebles'),
    ]

    operations = [
        migrations.AddField(
            model_name='inmuebles',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]