# Generated by Django 2.2.5 on 2019-09-19 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20190917_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=True),
        ),
    ]
