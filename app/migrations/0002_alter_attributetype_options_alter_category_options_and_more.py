# Generated by Django 5.1.4 on 2025-01-22 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attributetype',
            options={'verbose_name': 'Attribute Type', 'verbose_name_plural': 'Attribute Types'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='memory',
            options={'verbose_name': 'Memory', 'verbose_name_plural': 'Memories'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterModelOptions(
            name='productimage',
            options={'verbose_name': 'Product Image', 'verbose_name_plural': 'Product Images'},
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='repairservice',
            name='fix_time',
            field=models.DateTimeField(),
        ),
    ]
