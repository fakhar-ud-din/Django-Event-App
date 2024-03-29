# Generated by Django 2.2.4 on 2019-08-08 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20190802_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='email_address',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Email Address'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='phone',
            field=models.CharField(blank=True, max_length=11, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='website',
            field=models.URLField(blank=True, verbose_name='Website'),
        ),
    ]
