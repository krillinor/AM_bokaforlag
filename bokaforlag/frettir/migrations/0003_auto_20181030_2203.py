# Generated by Django 2.0.9 on 2018-10-30 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frettir', '0002_auto_20181030_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frett',
            name='texti',
            field=models.TextField(max_length=2000, verbose_name='Texti'),
        ),
    ]
