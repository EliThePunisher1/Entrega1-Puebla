# Generated by Django 4.0.3 on 2022-03-24 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='modelo3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=10)),
                ('apellido', models.CharField()),
                ('contraseña', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
