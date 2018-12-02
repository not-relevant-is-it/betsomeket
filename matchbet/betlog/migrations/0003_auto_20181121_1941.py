# Generated by Django 2.1.2 on 2018-11-21 19:41

import betlog.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('betlog', '0002_auto_20181121_1837'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='site',
            name='balance_currency',
        ),
        migrations.AlterField(
            model_name='site',
            name='balance',
            field=betlog.models.MyMoneyField(decimal_places=2, default=0, editable=False, max_digits=14, verbose_name='Balance'),
        ),
    ]
