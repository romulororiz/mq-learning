# Generated by Django 3.1.2 on 2020-11-03 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workshop',
            name='subtitle',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]