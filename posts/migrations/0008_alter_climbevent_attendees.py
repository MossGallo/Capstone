# Generated by Django 4.0.5 on 2022-06-24 18:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0007_climbevent_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='climbevent',
            name='attendees',
            field=models.ManyToManyField(blank=True, related_name='attending_events', to=settings.AUTH_USER_MODEL),
        ),
    ]
