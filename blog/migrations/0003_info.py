# Generated by Django 2.2.2 on 2020-02-12 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0002_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='제목')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='설명')),
                ('content', models.TextField(verbose_name='본문')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='작성시각')),
                ('modify_date', models.DateTimeField(auto_now=True, verbose_name='수정시각')),
            ],
        ),
    ]