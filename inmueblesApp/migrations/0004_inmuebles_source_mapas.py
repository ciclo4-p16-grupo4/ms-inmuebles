# Generated by Django 3.2.8 on 2021-12-13 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmueblesApp', '0003_inmuebles_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='inmuebles',
            name='source_mapas',
            field=models.TextField(db_index=True, null=True),
        ),
    ]
