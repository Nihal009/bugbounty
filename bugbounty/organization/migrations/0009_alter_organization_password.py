# Generated by Django 5.1.2 on 2024-10-28 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0008_alter_organization_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='password',
            field=models.CharField(max_length=128),
        ),
    ]
