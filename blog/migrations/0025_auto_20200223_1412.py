# Generated by Django 2.2.2 on 2020-02-23 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_consult'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consult',
            name='name',
            field=models.CharField(max_length=400, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='consult',
            name='phone',
            field=models.CharField(max_length=400, verbose_name='phone'),
        ),
    ]
