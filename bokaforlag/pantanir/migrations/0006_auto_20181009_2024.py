# Generated by Django 2.0.9 on 2018-10-09 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pantanir', '0005_auto_20181009_2017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pontun',
            name='magn',
        ),
        migrations.AddField(
            model_name='pontun',
            name='verd',
            field=models.PositiveIntegerField(null=True, verbose_name='Verð'),
        ),
    ]
