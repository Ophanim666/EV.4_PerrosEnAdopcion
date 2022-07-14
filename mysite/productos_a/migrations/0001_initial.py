# Generated by Django 4.0.5 on 2022-07-13 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fotografia', models.ImageField(upload_to='docentes')),
                ('codigo', models.CharField(max_length=15)),
                ('nombre', models.CharField(max_length=50)),
                ('categoria', models.CharField(choices=[('Alimentos', 'Alimentos'), ('Juguetes', 'Juguetes'), ('Magister', 'Magister')], max_length=50)),
            ],
        ),
    ]
