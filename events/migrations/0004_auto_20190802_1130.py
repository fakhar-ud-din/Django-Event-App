# Generated by Django 2.2.4 on 2019-08-02 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20190802_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='venue',
            field=models.CharField(max_length=120),
        ),
    ]
