# Generated by Django 2.2.4 on 2019-08-02 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Venue Name')),
                ('address', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=10, verbose_name='Zip/Postal Code')),
                ('phone', models.CharField(max_length=11, verbose_name='Phone Number')),
                ('email_address', models.EmailField(max_length=254, verbose_name='Email Address')),
                ('website', models.URLField(verbose_name='Website')),
            ],
        ),
    ]