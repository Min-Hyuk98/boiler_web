# Generated by Django 2.2.2 on 2020-02-23 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20200223_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consult',
            name='phone',
            field=models.CharField(max_length=11, verbose_name='phone'),
        ),
    ]