# Generated by Django 2.0.9 on 2018-10-30 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frettir', '0003_auto_20181030_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frett',
            name='titill',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Titill'),
        ),
    ]
