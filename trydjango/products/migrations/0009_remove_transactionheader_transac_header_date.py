# Generated by Django 2.2.5 on 2019-09-27 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20190927_1530'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactionheader',
            name='transac_header_date',
        ),
    ]
