# Generated by Django 4.0.1 on 2022-01-31 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='photo',
        ),
    ]
