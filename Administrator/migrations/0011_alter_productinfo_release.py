# Generated by Django 3.2.9 on 2021-12-07 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administrator', '0010_alter_productinfo_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinfo',
            name='release',
            field=models.CharField(default='否', max_length=5, verbose_name='是否已发布'),
        ),
    ]
