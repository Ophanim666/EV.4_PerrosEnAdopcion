# Generated by Django 4.0.5 on 2022-07-13 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0003_rename_perro_dueño_perros'),
    ]

    operations = [
        migrations.AddField(
            model_name='perro',
            name='imagen',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
