# Generated by Django 4.0.5 on 2022-06-10 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mountain',
            old_name='approach',
            new_name='route',
        ),
    ]
