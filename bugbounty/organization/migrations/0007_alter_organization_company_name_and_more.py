# Generated by Django 5.1.2 on 2024-10-28 08:49

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0006_alter_organization_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='company_name',
            field=models.CharField(default='default_name', max_length=255),
        ),
        migrations.AlterField(
            model_name='organization',
            name='email',
            field=models.EmailField(default='default_email', max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
    ]