# Generated by Django 2.2.2 on 2020-02-20 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_aircon_boiler_onsugi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aircon',
            name='aircon_type',
            field=models.CharField(max_length=100, verbose_name='에어컨종류'),
        ),
    ]