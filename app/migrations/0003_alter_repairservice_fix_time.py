# Generated by Django 5.1.4 on 2025-01-22 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_attributetype_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repairservice',
            name='fix_time',
            field=models.CharField(max_length=10),
        ),
    ]
