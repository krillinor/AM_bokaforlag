# Generated by Django 2.0.9 on 2018-10-30 22:54

import bokaforlag.frettir.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frettir', '0004_auto_20181030_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='frett',
            name='mynd',
            field=models.ImageField(blank=True, upload_to=bokaforlag.frettir.models.frettamynd_path),
        ),
    ]
