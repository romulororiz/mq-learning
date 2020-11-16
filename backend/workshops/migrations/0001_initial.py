# Generated by Django 3.1.2 on 2020-11-13 13:11

from django.conf import settings
from django.db import migrations, models
import workshops.models


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
                ('subtitle', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField()),
                ('banner', models.ImageField(blank=True, upload_to=workshops.models.user_directory_path)),
                ('location', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now=True)),
                ('date_start', models.DateTimeField()),
                ('date_end', models.DateTimeField()),
                ('category', models.CharField(blank=True, choices=[('self', 'Self'), ('work', 'Work'), ('rela', 'Relations')], max_length=9)),
                ('link', models.URLField(blank=True)),
                ('cost', models.IntegerField()),
                ('max_seats', models.IntegerField(default=20)),
                ('attendees', models.ManyToManyField(blank=True, related_name='m2m_workshops', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
