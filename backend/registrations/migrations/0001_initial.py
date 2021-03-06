# Generated by Django 3.1.2 on 2020-11-16 14:50

from django.db import migrations, models
import registrations.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PasswordReset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=registrations.models.code_generator, max_length=5)),
                ('code_used', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='RegistrationProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=registrations.models.code_generator, max_length=5)),
                ('code_used', models.BooleanField(default=False)),
            ],
        ),
    ]
