# Generated by Django 2.0.9 on 2018-10-09 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pantanir', '0004_auto_20181009_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pontun',
            name='bok',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bok', to='baekur.Bok', verbose_name='Bók'),
        ),
    ]
