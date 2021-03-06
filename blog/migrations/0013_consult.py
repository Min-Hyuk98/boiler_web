# Generated by Django 2.2.2 on 2020-02-22 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20200220_1125'),
    ]

    operations = [
        migrations.CreateModel(
            name='consult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='name')),
                ('phone', models.IntegerField(verbose_name='phone')),
                ('content', models.CharField(max_length=400, verbose_name='content')),
                ('time', models.DateField(verbose_name='time')),
                ('reply', models.CharField(max_length=400, verbose_name='reply')),
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
