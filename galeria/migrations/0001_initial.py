# Generated by Django 3.2.19 on 2023-05-22 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='motosicleta')),
                ('titulo', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=20)),
                ('precio', models.IntegerField()),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'galeria',
                'verbose_name_plural': 'galerias',
            },
        ),
    ]
