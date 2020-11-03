# Generated by Django 3.1.2 on 2020-11-03 05:46

from django.db import migrations, models
import registrations.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=registrations.models.code_generator, max_length=5)),
                ('code_used', models.BooleanField(default=False)),
            ],
        ),
    ]