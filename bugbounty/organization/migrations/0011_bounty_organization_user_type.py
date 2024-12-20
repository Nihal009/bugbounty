# Generated by Django 5.1.2 on 2024-10-30 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0010_alter_organization_company_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bounty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('status', models.BooleanField(default=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='organization',
            name='user_type',
            field=models.CharField(default='organization', max_length=20),
        ),
    ]
