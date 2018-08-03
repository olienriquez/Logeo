# Generated by Django 2.0.7 on 2018-08-03 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Logeo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(help_text='Nombre de usuario', max_length=30)),
                ('password', models.CharField(help_text='Contraseña', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(help_text='Nombre de usuario', max_length=30, primary_key=True, serialize=False)),
                ('password1', models.CharField(help_text='Contraseña', max_length=30)),
                ('password2', models.CharField(help_text='Confirmacion de contraseña', max_length=30)),
                ('first_name', models.CharField(help_text='Nombre', max_length=30)),
                ('last_name', models.CharField(help_text='Apellido', max_length=30)),
                ('email', models.EmailField(help_text='Correo electronico', max_length=254)),
            ],
        ),
    ]
