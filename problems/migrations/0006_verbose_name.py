# Generated by Django 5.1.3 on 2024-11-29 18:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0005_base_catrgory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problems',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='problems.categories', verbose_name='Категория'),
        ),
    ]
