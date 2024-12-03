# Generated by Django 4.2.16 on 2024-12-03 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0017_alter_bounty_max_reward_alter_bounty_min_reward'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bounty',
            name='max_reward',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Maximum reward amount', max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='bounty',
            name='min_reward',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Minimum reward amount', max_digits=10, null=True),
        ),
    ]