# Generated by Django 4.0.5 on 2022-06-27 01:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dueño',
            old_name='carrera',
            new_name='perro',
        ),
    ]
