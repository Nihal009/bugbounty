# Generated by Django 5.1.2 on 2024-10-27 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0002_admin_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
        migrations.DeleteModel(
            name='Admin',
        ),
    ]
