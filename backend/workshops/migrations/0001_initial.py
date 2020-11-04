# Generated by Django 3.1.2 on 2020-11-03 17:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now=True)),
                ('date_start', models.DateTimeField()),
                ('date_end', models.DateTimeField()),
                ('cost', models.IntegerField()),
                ('attendees', models.ManyToManyField(related_name='m2m_workshops', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
