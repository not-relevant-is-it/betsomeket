# Generated by Django 2.1.2 on 2018-11-02 18:21

import betlog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('betlog', '0005_auto_20181102_1805'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='site',
            name='balance_currency',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='balanceAdjust_currency',
        ),
        migrations.AlterField(
            model_name='site',
            name='balance',
            field=betlog.models.MyMoneyField(decimal_places=2, default=0, editable=False, max_digits=14, verbose_name='Balance'),
        ),
        migrations.AlterField(
            model_name='site',
            name='comment',
            field=models.CharField(blank=True, default='None', max_length=255, verbose_name='Comments'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='balanceAdjust',
            field=betlog.models.MyMoneyField(decimal_places=2, default=10.0, max_digits=7, verbose_name='Balance Adjust'),
        ),
    ]