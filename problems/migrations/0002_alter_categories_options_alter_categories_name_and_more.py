# Generated by Django 5.0.6 on 2024-05-23 09:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name': 'Категорию', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterField(
            model_name='categories',
            name='name',
            field=models.CharField(max_length=120, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='URL'),
        ),
        migrations.CreateModel(
            name='Problems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Названии проблемы')),
                ('description', models.TextField(blank=True, max_length=255, null=True, verbose_name='Описание проблемы')),
                ('address', models.CharField(max_length=150, verbose_name='Адресс проблемы')),
                ('image', models.ImageField(upload_to='problems_images', verbose_name='Изображение проблемы')),
                ('image_resolved', models.ImageField(upload_to='problems_images_resolved', verbose_name='Изображение решенной проблемы')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='URL')),
                ('status', models.CharField(choices=[('New', 'Новая'), ('Rejected', 'Отклонена'), ('Success', 'Решена')], default='New', max_length=20, verbose_name='Статус')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='problems.categories')),
            ],
            options={
                'verbose_name': 'Проблему',
                'verbose_name_plural': 'Проблемы',
                'db_table': 'problem',
            },
        ),
    ]
