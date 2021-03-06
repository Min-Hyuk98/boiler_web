# Generated by Django 2.2.2 on 2020-02-23 05:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_delete_consult'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='name')),
                ('phone', models.CharField(max_length=11, verbose_name='phone')),
                ('content', models.CharField(max_length=400, verbose_name='content')),
                ('time', models.DateField(default=datetime.datetime.today, verbose_name='time')),
                ('reply', models.CharField(blank=True, max_length=400, verbose_name='reply')),
                ('p1', models.CharField(blank=True, max_length=100, verbose_name='p1')),
                ('p2', models.CharField(blank=True, max_length=100, verbose_name='p2')),
                ('p3', models.CharField(blank=True, max_length=100, verbose_name='p3')),
                ('p4', models.CharField(blank=True, max_length=100, verbose_name='p4')),
                ('i1', models.IntegerField(blank=True, null=True, verbose_name='i1')),
                ('i2', models.IntegerField(blank=True, null=True, verbose_name='i2')),
                ('i3', models.IntegerField(blank=True, null=True, verbose_name='i3')),
            ],
        ),
    ]
