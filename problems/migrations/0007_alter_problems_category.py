# Generated by Django 5.1.3 on 2024-11-29 19:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0006_verbose_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problems',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='problems.categories'),
        ),
    ]